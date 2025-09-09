import gzip
import io
import glob

# Purpose: Extracts IP addresses from a single gzipped log file that accessed /robots.txt
def find_robots(filename):
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[2])
    return robots
    
# Purpose: Processes all gzipped log files in a directory
def find_all_robots(logdir):
    files = glob.glob(f"{logdir}/*.log.gz")
    all_robots = set()
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots

# For I/O-bound operations (like file reading, network requests) 
# Use threads for parallel execution
# For CPU-bound operations (like mathematical computations)
# Use processes for parallel execution

from concurrent import futures

# Parallel version using ProcessPoolExecutor
def find_all_robots_parallel(logdir):
    files = glob.glob(f"{logdir}/*.log.gz")
    all_robots = set()
    # Uses separate processes instead of threads
    with futures.ProcessPoolExecutor() as executor:
        for robots in executor.map(find_robots, files):
            all_robots.update(robots)
    return all_robots

if __name__ == "__main__":
    robots = find_all_robots("/data/logs")
    for ipaddr in robots:
        print(ipaddr)

    robots = find_all_robots_parallel("/data/logs")
    for ipaddr in robots:
        print(ipaddr)