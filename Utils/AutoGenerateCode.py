from Cheetah.Template import Template
import json
from urllib.parse import quote
import os
from Utils.Contants import generalTmpl

filePath = os.path.join(os.path.dirname(__file__), '../Template/news')


def autoGenerateCode(name, source, seed_url, listXPaths, detailXPaths, kwargs, transferOp, dateTimeFmt=None, fileDir=None):
    start_cmd = f"""
    # python {name}.py --seed_url="{seed_url}" --period="['20210101', '20210702']"
    """
    with open(generalTmpl, 'r', encoding='utf-8') as fr:
        generateTpl = fr.read()

    # listXPaths, detailXPaths, kwargs, start_cmd
    nameSpace = dict(
        listXPaths=listXPaths,
        detailXPaths=detailXPaths,
        kwargs=kwargs,
        start_cmd=start_cmd,
        seed_url=f"'{seed_url}'",
        source=f"'{source}'",
        transferOp = transferOp,
        dateTimeFormat = (dateTimeFmt and f"'{dateTimeFmt}'") or "'%Y-%m-%d %H:%M:%S'"
    )
    t = Template(generateTpl, searchList=[nameSpace])
    fileName = os.path.join(fileDir or filePath, f"{name}.py")
    with open(fileName, 'w', encoding='utf-8') as fw:
        fw.write(t.respond())