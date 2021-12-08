import psutil as ps


def get_cpu():
    info = {
        'user': ps.cpu_times().user,
        'system': ps.cpu_times().system,
        'idle': ps.cpu_times().idle,
    }
    return info


def get_network():
    result = {
        'data': ps.net_io_counters(pernic=False),
    }
    return result


def get_memory():
    info = {
        'total': ps.virtual_memory().total,
        'available': ps.virtual_memory().available,
        'used': ps.virtual_memory().active,
        'free': ps.virtual_memory().inactive,
    }
    return info


def get_disks():
    info = {
        'disk': ps.disk_usage('/')
    }
    return info


def get_process():
    p = ps.Process()
    p.as_dict(attrs=['pid', 'name', 'username'])
    return p


def show(**kwargs):
    print(kwargs['cpu'])
    print(kwargs['network'])
    print(kwargs['memory'])
    print(kwargs['disk'])
    print(kwargs['process'])


def run():
    cpu = get_cpu()
    network = get_network()
    memory = get_memory()
    disk = get_disks()
    process = get_process()
    show(cpu=cpu,
         network=network,
         memory=memory,
         disk=disk,
         process=process
         )


if __name__ == "__main__":
    run()