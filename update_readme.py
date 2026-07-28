import json
from datetime import datetime


RESULT_FILE = "results/latest_result.json"

README_FILE = "README.md"



with open(
    RESULT_FILE,
    "r"
) as file:

    data = json.load(file)




with open(
    README_FILE,
    "r"
) as file:

    readme = file.read()




start = "<!-- OPTIMIZATION_RESULTS_START -->"

end = "<!-- OPTIMIZATION_RESULTS_END -->"



new_section = f"""
{start}

## Latest Optimization Result

| Parameter | Value |
|---|---|
| Amplitude | {data['amplitude']:.6f} |
| Duration | {data['duration']:.6f} |
| Fidelity | {data['fidelity']:.10f} |
| Leakage | {data['leakage']:.10f} |

Last Updated:

{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

{end}
"""



if start in readme and end in readme:


    before = readme.split(start)[0]

    after = readme.split(end)[1]


    readme = (
        before
        +
        new_section
        +
        after
    )


else:


    readme += "\n" + new_section




with open(
    README_FILE,
    "w"
) as file:

    file.write(
        readme
    )


print(
    "README updated successfully"
)