# 🌟 SECRETLY YOU — Pygame Game

A Stardew Valley-style visual novel game based on the Secretly You story.
Play as Aya (Starlace) and explore your small town while triggering all 22 story scenes.

---

## 🚀 HOW TO RUN

1. Make sure Python 3.8+ is installed
2. Install pygame:
   ```
   pip install pygame
   ```
3. Run the game:
   ```
   cd secretly_you
   python main.py
   ```

---

## 🎮 CONTROLS

| Key | Action |
|-----|--------|
| WASD / Arrow Keys | Move player |
| E or Enter | Interact with NPCs / Trigger scenes |
| Space | Advance dialog |
| ↑ ↓ | Select choices in dialog |
| F5 | Save game |
| L (on title) | Load saved game |
| ESC | Pause menu |

---

## 🗂️ PROJECT STRUCTURE

```
secretly_you/
├── main.py                     ← Entry point (run this)
├── requirements.txt
├── save_data.json              ← Auto-generated save file
│
├── engine/
│   ├── game.py                 ← Main game loop & state machine
│   ├── asset_manager.py        ← Image/font loader + placeholder generator
│   ├── player.py               ← Player movement & animation
│   ├── camera.py               ← Smooth follow camera
│   ├── dialog_system.py        ← Typewriter dialog + choices + phone mode
│   ├── game_state.py           ← Save/load, scene flags, progress tracking
│   ├── world.py                ← Maps, NPCs, trigger zones, portals
│   ├── map_builder.py          ← All map definitions with triggers/NPCs
│   ├── hud.py                  ← HUD, minimap, notifications
│   └── scene_manager.py        ← Scene playback with fade transitions
│
├── scenes/
│   └── scene_data.py           ← All 22 scenes with full dialog
│
└── assets/
    └── images/
        ├── characters/         ← Drop character sprites here
        ├── maps/               ← Drop map/tileset images here
        ├── ui/                 ← Drop UI elements here
        └── backgrounds/        ← Drop scene backgrounds here
```

---

## 🖼️ REPLACING PLACEHOLDER IMAGES

The game auto-generates colored placeholder graphics so it runs immediately.
To use your own images:

1. Place your image files in the matching `assets/images/` subfolder
2. Name them to match the asset keys below
3. Restart the game — it auto-loads any `.png`, `.jpg`, `.jpeg`, `.bmp` files found

### Character images (120×200 px recommended):
- `aya_idle.png`, `aya_happy.png`, `aya_sad.png`, `aya_angry.png`, `aya_shocked.png`, `aya_smirk.png`
- `ren_idle.png`, `ren_happy.png`, `ren_sad.png`, `ren_cold.png`, `ren_shocked.png`, `ren_smile.png`
- `ms_pearl.png`, `marco.png`, `chloe.png`, `mika.png`, `leah.png`, `kenji.png`, `adrian.png`

### Player walk sprites (48×64 px recommended, top-down):
- `player_down_0.png`, `player_down_1.png`, `player_down_2.png`
- `player_up_0.png`, `player_up_1.png`, `player_up_2.png`
- `player_left_0.png`, `player_left_1.png`, `player_left_2.png`
- `player_right_0.png`, `player_right_1.png`, `player_right_2.png`

### Maps (large, scrollable):
- `map_town.png`   — 2560×1440 px (town area)
- `map_school.png` — 2560×1440 px (school interior)

### Scene backgrounds (1280×720 px):
- `bg_online.png`       — dark phone/chat screen
- `bg_classroom.png`    — school classroom
- `bg_afterschool.png`  — evening / night mood
- `bg_hallway.png`      — school hallway
- `bg_rooftop.png`      — rooftop sunset
- `bg_gym.png`          — graduation gymnasium
- `bg_school_gate.png`  — school entrance
- `bg_night_room.png`   — bedroom at night

---

## 📖 STORY PROGRESSION

Scenes unlock automatically as you complete previous ones.
Walk into glowing portal zones or highlighted areas to trigger scenes.
Yellow dots on the minimap show unfinished trigger zones.

**Scene order:**
1 → Online Chat (Town) → 2 → Classroom → 3 → After School (Night Room) → 4 → Friend Groups → 5 → Partners → 6 → Clues → 7 → Discovery → 8 → THE REVEAL → 9 → Awkward Phase → 10 → Inner Conflict → 11 → Project → 12 → The Truth → 13 → Rooftop → 14 → Confession → 15 → Decision → 16 → Resolution → 17 → Graduation → 18 → Quiet Moment → 19 → Last Chat → 20 → The Promise → 21 → Farewell → 22 → FINAL TWIST ✨

---

## 💡 TIPS FOR DEVELOPERS

- Add new scenes in `scenes/scene_data.py`
- Add new maps in `engine/map_builder.py`
- Add new NPCs with: `map.add_npc(NPC("Name", x, y, "portrait_key", "dialog_key"))`
- Add new trigger zones with: `map.add_trigger("name", x, y, w, h, "scene_N")`
- Story flags: `game_state.set_flag("flag_name")` / `game_state.get_flag("flag_name")`

---

*"Some stories don't end after graduation… Sometimes they just begin again."*
