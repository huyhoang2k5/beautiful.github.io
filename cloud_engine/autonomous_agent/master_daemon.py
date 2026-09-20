"""
MASTER AUTONOMOUS MONEY-SEEKING DAEMON
Tự động kích hoạt Autonomous Orchestrator theo chu kỳ của scheduler (task-286)
"""

import os
import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENGINE_DIR = os.path.join(BASE_DIR, "engine")
if ENGINE_DIR not in sys.path:
    sys.path.insert(0, ENGINE_DIR)

from autonomous_orchestrator import run_pipeline

def main():
    print(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] KÍCH HOẠT CHU KỲ KIẾM TIỀN TỰ ĐỘNG...")
    run_pipeline()

if __name__ == "__main__":
    main()
