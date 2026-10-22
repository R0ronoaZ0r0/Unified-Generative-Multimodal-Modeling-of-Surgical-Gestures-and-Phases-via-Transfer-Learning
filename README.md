## TODO:
- [x] Train phase model on JIGSAWS dataset
- [x] Transfer Learning
    - [x] Gesture From Scratch
    - [x] Phase From Scratch
    - [x] Phase Full Model Fine Tuning
    - [x] Phase Frozen Encoder
    - [x] Phase Linear Probe

- [x] Pareto Fronts
    - [x] Gesture From Scratch
    - [x] Phase From Scratch
    - [x] Phase Full Model Fine Tuning
    - [x] Phase Frozen Encoder
    - [x] Phase Linear Probe

- [x] Ablation study (visual, action, language, and time)
    - [x] Remove one modality
    - [x] Remove two modalities
    - [x] Remove three modalities (vision only)

- [x] Add the prediction and generation of GRS scores to the model
    - [x] Train GRS model on JIGSAWS dataset

## Data:
- JIGSAWS dataset provides videos, kinematics, Global Rating Scale (GRS) scores, and gesture annotations
- Videos sampled every 5 frames
- Suturing sample count: 10,504
- Knot Tying sample count: 4,926
- Needle Passing sample count: 7,270

## Gesture and Phase Mappings:
### Gesture Labels:
- (G1) reaching for the needle with right hand;
- (G2) positioning the tip of the needle;
- (G3) pushing needle through the tissue;
- (G4) transferring needle from left to right;
- (G5) moving to center of workspace with needle in grip;
- (G6) pulling suture with left hand;
- (G7) pulling suture with right hand;
- (G8) orienting needle;
- (G9) using right hand to help tighten suture;
- (G10) loosening more suture;
- (G11) dropping suture and moving to end points;
- (G12) reaching for needle with left hand;
- (G13) making C loop around right hand;
- (G14) reaching for suture with right hand;
- (G15) pulling suture with both hands.

### Phase Labels:
- Phase 1 (Needle Preparation) - (G1, G5, G8, G12)
- Phase 2 (Needle Positioning) - (G2)
- Phase 3 (Needle Driving) - (G3)
- Phase 4 (Suture Management) - (G6, G7, G9, G15)
- Phase 5 (Transfer/Handoff) - (G4, G13, G14)
- Phase 6 (Completion) - (G10, G11)

### Gesture used in each task:
- Suturing:  1, 2, 3, 4, 5, 6, 8, 9, 10, 11
- Knot_Tying: 1 , 11 , 12 , 13 , 14 , 15
- NeedlePassing: 1, 2, 3, 4, 5, 6, 8, 11


## Mapping Table

| **Phase ID** | **Phase Name**                     | **Gestures (Code + Description)**                                                                                                                                       | **Tasks Involved**                   |
| :----------: | :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
|    **P1**    | **Needle Preparation**             | G1 – Reaching for needle with right hand<br>G5 – Moving to center of workspace with needle in grip<br>G8 – Orienting needle<br>G12 – Reaching for needle with left hand | Suturing, Knot Tying, Needle Passing |
|    **P2**    | **Needle Positioning**             | G2 – Positioning the needle tip at the intended entry point                                                                                                             | Suturing, Needle Passing             |
|    **P3**    | **Needle Driving**                 | G3 – Pushing the needle through the tissue                                                                                                                              | Suturing, Needle Passing             |
|    **P4**    | **Suture Management**              | G6 – Pulling suture with left hand<br>G7 – Pulling suture with right hand<br>G9 – Using right hand to help tighten suture<br>G15 – Pulling suture with both hands       | Suturing, Knot Tying                 |
|    **P5**    | **Transfer / Handoff**             | G4 – Transferring needle from left to right hand<br>G13 – Making C-loop around right hand<br>G14 – Reaching for suture with right hand                                  | Suturing, Knot Tying, Needle Passing |
|    **P6**    | **Completion / Final Positioning** | G10 – Loosening more suture<br>G11 – Dropping suture and moving to end points                                                                                           | Suturing, Knot Tying, Needle Passing |


### GRS (Global Rating Scale) Components

The JIGSAWS dataset includes 6 GRS components rated on a scale of 1-5:
- Respect for tissue : 0
- Suture/needle handling : 1
- Time and motion : 2
- Flow of operation : 3
- Overall performance : 4
- Quality of final product : 5