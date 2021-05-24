#!/usr/bin/env python


import psutil
from psadmin import graphite, base

USER_NAME = "yb"


def main():
    proc_list = [
        proc
        for proc in psutil.process_iter(["username"])
        if proc.username() == USER_NAME
    ]

    stats = {}
    for proc in proc_list:
        try:
            if proc.name() == "uwsgi" and proc.cmdline()[2] == "zergpool":
                short_name = proc.cmdline()[7].split("/")[-1][:-4]
            elif proc.name() == "uwsgi":
                short_name = proc.cmdline()[6].split("/")[-1].rsplit(".")[0]
            elif proc.name().split("/")[-1] == "python":
                if len(proc.cmdline()) > 1:
                    if proc.cmdline()[1] == "-m":
                        short_name = proc.cmdline()[2]
                    else:
                        t = proc.cmdline()[1].split("/")
                        short_name = "{}_{}".format(t[3].rsplit(".")[0], t[-1])
                else:
                    continue
            else:
                short_name = "other"

            if stats.get(proc.ppid()):
                stats[proc.ppid()]["cpu_usage"] += proc.cpu_percent(interval=0.1)
            else:
                stats[proc.ppid()] = {
                    "cpu_usage": proc.cpu_percent(interval=0.1),
                    "short_name": short_name.replace(".", "_"),
                }
        except (psutil.AccessDenied, psutil.ZombieProcess, psutil.NoSuchProcess):
            continue
        except IndexError:
            print(proc.cmdline())
    metrics = {value["short_name"]: value["cpu_usage"] for value in stats.values()}
    metric_path = ".".join(["one_min", graphite.undescored_fqdn(), "services"])
    m = graphite.prepare_metrics_from_dict(metric_path, metrics)
    check_name = "cpu_load_stats_by_trust"
    status = "ERROR"
    msg = "Failed send metrics to graphite"
    if graphite.send(m):
        status = "OK"
        msg = "Successfully sent metrics to grphite"
    base.monrun_output(check_name, status, msg)


if __name__ == "__main__":
    main()
