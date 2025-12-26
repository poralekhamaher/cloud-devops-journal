import argparse
import logging
import sys
import os
import shutil

def setup_logging():
    """Configure logging to both file and console"""
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("logs/run.log"),
            logging.StreamHandler()
        ]
    )

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Multi-mode operations tool")
    parser.add_argument("--mode", required=True, choices=["evens", "scan", "health"],
                       help="Operation mode: evens, scan, or health")
    parser.add_argument("--name", help="Your name (required for evens mode)")
    parser.add_argument("--number", type=int, help="Max number (required for evens mode)")
    parser.add_argument("--logfile", default="app.log", help="Log file to scan (for scan mode)")
    return parser.parse_args()

def generate_evens(number):
    """Generate list of even numbers from 1 to number"""
    return [str(i) for i in range(1, number + 1) if i % 2 == 0]

def write_evens_output(name, evens):
    """Write even numbers to output.txt"""
    results = [f"User: {name}"] + evens
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(results) + "\n")
    logging.info(f"Wrote {len(evens)} even numbers to output.txt")

def mode_evens(args):
    """Handle evens mode: generate even numbers"""
    if not args.name or not args.number:
        logging.error("--name and --number required for evens mode")
        return 1
    
    name = args.name.strip().title()
    evens = generate_evens(args.number)
    write_evens_output(name, evens)
    return 0

def mode_scan(args):
    """Handle scan mode: scan logs for ERROR and WARNING"""
    if not os.path.exists(args.logfile):
        logging.error(f"Log file not found: {args.logfile}")
        return 1
    
    os.makedirs("output", exist_ok=True)
    flagged = []
    
    with open(args.logfile, "r", encoding="utf-8") as f:
        for line in f:
            if "ERROR" in line or "WARNING" in line:
                flagged.append(line.rstrip())
    
    if not flagged:
        logging.info("No ERROR or WARNING entries found")
        return 2
    
    output_path = "output/flagged.log"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(flagged) + "\n")
    
    logging.info(f"Found {len(flagged)} flagged entries, written to {output_path}")
    return 0

def mode_health(args):
    """Handle health mode: collect system metrics"""
    try:
        import psutil
    except ImportError:
        logging.error("psutil not installed. Run: pip install psutil")
        return 1
    
    try:
        disk = shutil.disk_usage("/")
        disk_percent = (disk.used / disk.total) * 100
        
        cpu_percent = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        mem_percent = mem.percent
        
        logging.info(f"Disk: {disk_percent:.1f}% | CPU: {cpu_percent:.1f}% | Memory: {mem_percent:.1f}%")
        return 0
    except Exception as e:
        logging.error(f"Health check failed: {e}")
        return 3

def main():
    """Main entry point"""
    setup_logging()
    args = parse_args()
    
    try:
        if args.mode == "evens":
            return mode_evens(args)
        elif args.mode == "scan":
            return mode_scan(args)
        elif args.mode == "health":
            return mode_health(args)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return 3

if __name__ == "__main__":
    sys.exit(main())