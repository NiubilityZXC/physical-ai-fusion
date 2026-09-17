#!/usr/bin/env python3
"""local_asset_check.py — 本地模拟资产的可复核性检查(脚本化生成论文附录用数据)

输出 results/local-asset-check.json:
  1. zpinch 零维数据集:行数、E=½mv² 恒等式通过数(重算)
  2. SNOP 平均原子模型:由占据分布加权求和重算 Z̄,与 T_sbar.txt 程序输出比较
  3. FLASH 算例:flash.par.gpu 关键参数存在性检查(仅参数,不声称输出物理量)
"""
import json
import math
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
out = {"generated_by": "scripts/local_asset_check.py", "date": "2026-09-17"}

# 1. zpinch
z = zipfile.ZipFile("/home/user/zpinch_package_20260306/零维表格转换 (2).xlsx")
rows = []
for i in (1, 2):
    fn = f"xl/worksheets/sheet{i}.xml"
    if fn not in z.namelist():
        continue
    for row in ET.fromstring(z.read(fn)).iter(NS + "row"):
        vals = [float(v.text) if (v := c.find(NS + "v")) is not None and v.text else None
                for c in row.iter(NS + "c")]
        if len(vals) >= 7 and all(isinstance(x, float) for x in vals[:7]):
            rows.append(vals[:7])
ok = sum(1 for r in rows if abs(-math.sqrt(2e16 * r[5] / r[4]) - r[6]) / abs(r[6]) < 2e-4)
out["zpinch_0d"] = {"rows": len(rows), "identity_pass": ok,
                    "pass_fraction": ok / len(rows)}

# 2. SNOP occupation -> Zbar
p = []
for line in open("/home/user/Rosseland_opa_auto/Rosseland_opa_auto/nsp_out.txt"):
    if "nsp_out" in line:
        p.append(float(line.split("=")[1]))
zbar = sum(i * x for i, x in enumerate(p)) / sum(p)
tsbar = float(open("/home/user/Rosseland_opa_auto/Rosseland_opa_auto/T_sbar.txt").read().split()[1])
out["snop_average_atom"] = {
    "n_stages": len(p), "zbar_from_distribution": zbar,
    "zbar_program_output": tsbar,
    "relative_deviation": abs(zbar - tsbar) / tsbar}

# 3. FLASH par
par = Path("/home/user/FLASH_GPU_hydro_lab_20260715/flash.par.gpu").read_text()
out["flash_setup"] = {
    "par_file": "~/FLASH_GPU_hydro_lab_20260715/flash.par.gpu",
    "has_15ma_comment": "Ipeak=15MA" in par,
    "setup_line": [l for l in par.splitlines() if "setup -auto" in l][:1],
    "amr_lrefine_max": [l for l in par.splitlines() if "lrefine_max" in l and "=" in l][:1],
    "note": "parameters only; no output physics claimed",
}

(ROOT / "results").mkdir(exist_ok=True)
(ROOT / "results" / "local-asset-check.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2))
print(json.dumps(out, ensure_ascii=False, indent=2))
