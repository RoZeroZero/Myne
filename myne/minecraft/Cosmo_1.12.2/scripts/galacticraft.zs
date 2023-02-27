import crafttweaker.oredict.IOreDictEntry;
import mods.exnihilocreatio.Sieve;
import mods.exnihilocreatio.Hammer;
import mods.exnihilocreatio.Heat;

mods.exnihilocreatio.Hammer.addRecipe(<galacticraftcore:basic_block_moon:3>, <exnihilocreatio:block_dust>, 0, 1, 0.5);

mods.exnihilocreatio.Hammer.addRecipe(<galacticraftcore:basic_block_moon:4>, <galacticraftcore:basic_block_moon:5>, 0, 1, 0.5);

Sieve.addFlintMeshRecipe(<galacticraftcore:basic_block_moon:5>, <exnihilocreatio:item_ore_gold:0>, 0.05);


mods.exnihilocreatio.Hammer.addRecipe(<galacticraftplanets:mars:5>, <exnihilocreatio:block_dust>, 0, 1, 0.5);


mods.exnihilocreatio.Hammer.addRecipe(<galacticraftplanets:mars:9>, <galacticraftplanets:mars:6>, 0, 1, 0.5);

Sieve.addFlintMeshRecipe(<galacticraftplanets:mars:6>, <exnihilocreatio:item_ore_gold:0>, 0.05);

recipes.addShaped(<galacticraftplanets:venus:1>,
 [[<galacticraftplanets:venus:0>,<galacticraftplanets:venus:0>],
  [<galacticraftplanets:venus:0>,<galacticraftplanets:venus:0>]]);
  
mods.exnihilocreatio.Hammer.addRecipe(<galacticraftplanets:venus:1>, <galacticraftplanets:venus:0>, 0, 1, 0.5);
mods.exnihilocreatio.Hammer.addRecipe(<galacticraftplanets:venus:1>, <galacticraftcore:basic_item:2>, 0, 0.015, 0.5);


mods.exnihilocreatio.Heat.addRecipe(<galacticraftplanets:venus:2>, 2);
<ore:cobblestone>.add(<galacticraftplanets:mars:4>);
