# Unified Generative Multimodal Modeling of Surgical Gestures and Phases via Transfer Learning

Official code for the paper:

> **Unified Generative Multimodal Modeling of Surgical Gestures and Phases via Transfer Learning**<br>
> Hemanth Reddy Madduri, Xin Zhang, Jun Zheng, Huixin Zhan<br>
> *Proceedings of the 2026 ACM Southeast Conference (ACMSE 2026)*, pp. 93–102<br>
> [[Paper]](https://doi.org/10.1145/3746467.3801528)

## Getting Started

### 1. Install the dependencies

Use Python 3.10 or newer. Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Download the dataset

Download the [JIGSAWS dataset](https://cirl.lcsr.jhu.edu/research/hmm/datasets/jigsaws_release/) and arrange each task like this (the default location is `datasets/jigsaws`):

```
datasets/jigsaws/<Task>/video/*.avi
datasets/jigsaws/<Task>/transcriptions/*.txt
datasets/jigsaws/<Task>/meta_file_<Task>.txt
```

where `<Task>` is `Suturing`, `Needle_Passing` or `Knot_Tying`.

### 3. Edit `config.yaml`

All notebooks read their settings from [`config.yaml`](config.yaml) at the repository root, so this is the only file you need to edit:

- `paths`: where the dataset is and where features, models, training records, results and figures are written. Paths are relative to the repository root.
- `task`: the JIGSAWS task to preprocess and train on.
- `device`: `auto` (CUDA, then Apple Silicon, then CPU), or `cuda`, `mps` or `cpu`.
- `model` and `training`: model size and training hyperparameters used in the paper.

### 4. Run the notebooks

Open the notebooks in Jupyter (`jupyter lab`) and run all cells, in this order:

1. **Preprocessing:** `notebooks/preprocessing/preprocessing_jigsaws.ipynb` extracts ResNet-18 vision features and BERT language features and saves the train/test splits to `paths.features_dir`. The first run downloads the pretrained ResNet-18 and BERT weights.
2. **Gesture model:** `notebooks/diffusion_model/gesture_train.ipynb` trains the gesture model. It must run before the transfer learning notebooks, which fine-tune the saved model for the same task.
3. **Phase model from scratch:** `notebooks/diffusion_model/phase_train_from_scratch.ipynb`.
4. **Transfer learning:** the notebooks in `notebooks/transfer_learning/` fine-tune the gesture model for phase prediction (full model fine-tuning, frozen encoder and linear probe).
5. **Ablation study:** the notebooks in `notebooks/ablation/` train the phase model without one or more of the action, language and time inputs.
6. **GRS (optional):** `notebooks/diffusion_model/grs_train.ipynb` trains the model that also predicts the GRS scores.

Repeat steps 1–6 for each task by changing `task` in `config.yaml`.

7. **Figures:** once results exist for all three tasks, `notebooks/utils/pareto_front.ipynb` and `notebooks/utils/plots.ipynb` create the Pareto front and result plots in `paths.images_dir`.

Features, models, training records, results and figures are written to the folders under `outputs/` set in `config.yaml`, and re-running a notebook overwrites its previous files.

**Or run them with one command.** `run_pipeline.py` runs the notebooks in order for the task in `config.yaml`:

```bash
python run_pipeline.py
```

By default it runs preprocessing and the gesture, phase-from-scratch and GRS notebooks. Uncomment lines in its `PIPELINE` list to also run the transfer learning, ablation or figure notebooks. The notebooks themselves are not modified: an executed copy of each one, with all its cell outputs, is saved to `outputs/executed_notebooks/<task>/`, and the script stops at the first failure.

## Citation

If you find this work useful, please cite:

```bibtex
@inproceedings{madduri2026unified,
  title     = {Unified Generative Multimodal Modeling of Surgical Gestures and Phases via Transfer Learning},
  author    = {Madduri, Hemanth Reddy and Zhang, Xin and Zheng, Jun and Zhan, Huixin},
  booktitle = {Proceedings of the 2026 ACM Southeast Conference},
  series    = {ACMSE 2026},
  pages     = {93--102},
  year      = {2026},
  publisher = {Association for Computing Machinery},
  doi       = {10.1145/3746467.3801528},
  url       = {https://doi.org/10.1145/3746467.3801528}
}
```
