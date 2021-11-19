import psutil
import platform


class SystemInfo:

    def get_size(self, bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    def get_disk_size(self):
        # Disk Information
        disks_data = []

        partitions = psutil.disk_partitions()
        for partition in partitions:

            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue

            disk_data = {
                "device": partition.device,
                "mountPoint": partition.mountpoint,
                "fileSystemType": partition.fstype,
                "totalSize": self.get_size(partition_usage.total),
                "used": self.get_size(partition_usage.used),
                "free": self.get_size(partition_usage.free),
                "percentage": str(partition_usage.percent) + "%"

            }

            disks_data.append(disk_data)

        return disks_data

    def get_info(self):

        uname = platform.uname()
        cpufreq = psutil.cpu_freq()
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        net_io = psutil.net_io_counters()

        return {
            "system": {
                "system": uname.system,
                "nodeName": uname.node,
                "release": uname.release,
                "version": uname.version,
                "machine": uname.machine,
                "processor": uname.processor,
            },

            "cpu": {
                "physicalCores": psutil.cpu_count(logical=False),
                "totalCores": psutil.cpu_count(logical=True),
                "maxFrequency": str(cpufreq.max) + "Mhz",
                "minFrequency": str(cpufreq.min) + "Mhz",
                "currentFrequency": str(cpufreq.current) + "Mhz",
                "usage": str(psutil.cpu_percent()) + "%",
            },
            "memory": {
                "total": self.get_size(svmem.total),
                "available": self.get_size(svmem.available),
                "used": self.get_size(svmem.used),
                "percentage": str(swap.percent) + "%",
            },

            "disk": self.get_disk_size(),

            "network": {
                "sent": self.get_size(net_io.bytes_sent),
                "received": self.get_size(net_io.bytes_recv),
            }

        }
