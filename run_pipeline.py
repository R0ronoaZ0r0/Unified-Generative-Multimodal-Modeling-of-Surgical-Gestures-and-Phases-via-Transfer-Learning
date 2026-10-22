"""Run the pipeline notebooks in order for the task set in config.yaml.

Each notebook is executed in memory from its own folder, exactly as when it is
opened and run in Jupyter. The notebook files are not modified. An executed
copy of each notebook, with all its outputs, is saved to
paths.executed_notebooks_dir/<task>/, also when the notebook fails.

Usage:
    python run_pipeline.py

To run another task, change `task` in config.yaml and run the script again.
"""
import sys
import time
from pathlib import Path

import nbformat
import yaml
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

REPO_ROOT = Path(__file__).resolve().parent
NOTEBOOKS_DIR = REPO_ROOT / 'notebooks'

# Notebooks to run, in order. Comment a line out to skip that notebook.
PIPELINE = [
    # Preprocessing
    'preprocessing/preprocessing_jigsaws.ipynb',

    # From scratch
    'diffusion_model/gesture_train.ipynb',
    'diffusion_model/phase_train_from_scratch.ipynb',
    'diffusion_model/grs_train.ipynb',

    # Transfer learning (needs gesture_train.ipynb to have run for the same task)
    # 'transfer_learning/phase_train_full_model_fine_tuning.ipynb',
    # 'transfer_learning/phase_train_frozen_encoder.ipynb',
    # 'transfer_learning/phase_train_linear_probe.ipynb',

    # Ablation study
    # 'ablation/phase_train_w_o_language.ipynb',
    # 'ablation/phase_train_w_o_action.ipynb',
    # 'ablation/phase_train_w_o_time.ipynb',
    # 'ablation/phase_train_w_o_action_language.ipynb',
    # 'ablation/phase_train_w_o_action_time.ipynb',
    # 'ablation/phase_train_w_o_language_time.ipynb',
    # 'ablation/phase_train_vision_only.ipynb',

    # Figures (need results for all three tasks)
    # 'utils/pareto_front.ipynb',
    # 'utils/plots.ipynb',
]


def run_notebook(path, output_path):
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(
        nb,
        timeout=None,
        kernel_name='python3',
        resources={'metadata': {'path': str(path.parent)}},
    )
    try:
        client.execute()
    finally:
        # Save the executed copy, including the outputs up to a failing cell
        output_path.parent.mkdir(parents=True, exist_ok=True)
        nbformat.write(nb, output_path)


def main():
    with open(REPO_ROOT / 'config.yaml') as f:
        config = yaml.safe_load(f)
    task = config['task']
    executed_dir = REPO_ROOT / config['paths']['executed_notebooks_dir'] / task
    print(f"Task: {task}")

    for i, notebook in enumerate(PIPELINE, start=1):
        path = NOTEBOOKS_DIR / notebook
        output_path = executed_dir / notebook
        print(f"[{i}/{len(PIPELINE)}] {notebook} ...", flush=True)
        start = time.time()
        try:
            run_notebook(path, output_path)
        except CellExecutionError as error:
            print(f"\nFailed: {notebook}\n{error}", file=sys.stderr)
            print(f"Executed notebook saved to {output_path}", file=sys.stderr)
            sys.exit(1)
        print(f"    done in {time.time() - start:.0f}s, saved to {output_path.relative_to(REPO_ROOT)}", flush=True)

    print("Pipeline finished.")


if __name__ == '__main__':
    main()
