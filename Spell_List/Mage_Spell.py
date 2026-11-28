# This will contain every single spell with some set data that is standard to them.

GCD = 1.5

spell_template = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range" : [0.0,9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By": []
}

frostbolt = {
    "Name": "Frostbolt",
    "Mana Cost": 290,
    "Cast Time": 3.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range" : [470,505],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By": ["Arcane Instability", "Arcane Power", "Arctic Reach", "Clearcasting","Frost Channeling",
                    "Ice Barrier", "Ice Shards", "Improved Frostbolt", "Permafrost", "Piercing Ice", "Presence of Mind"
                    ]

}

frostfire_bolt = {
    "Name": "Frostfire Bolt",
    "Mana Cost": 370,
    "Cast Time": 3.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range" : [286,331],
    "DoT?": True,
    "DoT Damage Ticks": [19,19,19],
    "DoT Time Ticks": [6.0,3.0,0.0],
    "Affected By" : ["Accelerant","Arcane Instability","Arcane Power", "Burning Soul", "Clearcasting","Combustion",
                   "Critical Mass","Fire Blast","Ice Barrier","Ice Shards", "Permafrost", "Piercing Ice",
                   "Presence of Mind"
                   ]
}

arcane_blast = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range" : [0.0,9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By":[]
}

arcane_wrath = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range" : [0.0,9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By":[]
}

blizzard = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range" : [0.0,9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By":[]
}

pyroblast = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range" : [0.0,9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By":[]
}

fireball = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range" : [0.0,9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By":[]
}

blast_wave = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range": [0.0, 9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By": []
}

cone_of_cold = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range": [0.0, 9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By": []
}

scorch = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range": [0.0, 9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By": []
}

arcane_missiles = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range": [0.0, 9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By": []
}

ice_lance = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range": [0.0, 9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By": []
}

flamestrike = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range": [0.0, 9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By": []
}

fire_blast = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range": [0.0, 9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By": []
}

arcane_explosion = {
    "Name": "",
    "Mana Cost": 0,
    "Cast Time": 0.0,
    "Cooldown": GCD,
    "Resets 5-Second Regen?": True,
    "Instant Damage Range": [0.0, 9999.0],
    "DoT?": False,
    "DoT Damage Ticks": [],
    "DoT Time Ticks": [],
    "Affected By": []
}





spell_list = [frostbolt, frostfire_bolt, arcane_blast, arcane_wrath, blizzard, pyroblast, fireball, blast_wave,
              cone_of_cold, scorch, arcane_missiles, ice_lance, flamestrike, fire_blast, arcane_explosion]