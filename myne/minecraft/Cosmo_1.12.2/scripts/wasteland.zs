import mods.exnihilocreatio.Sieve;
import mods.exnihilocreatio.Hammer;

Sieve.addStringMeshRecipe(<ezwastelands:ezwastelandblock>, <exnihilocreatio:item_pebble>, 0.7);
Sieve.addFlintMeshRecipe(<ezwastelands:ezwastelandblock>, <exnihilocreatio:item_pebble>, 0.7);
Sieve.addFlintMeshRecipe(<ezwastelands:ezwastelandblock>, <exnihilocreatio:item_pebble>, 0.2);
Sieve.addIronMeshRecipe(<ezwastelands:ezwastelandblock>, <exnihilocreatio:item_pebble>, 0.7);
Sieve.addIronMeshRecipe(<ezwastelands:ezwastelandblock>, <exnihilocreatio:item_pebble>, 0.2);
Sieve.addIronMeshRecipe(<ezwastelands:ezwastelandblock>, <exnihilocreatio:item_pebble>, 0.1);
Sieve.addDiamondMeshRecipe(<ezwastelands:ezwastelandblock>, <exnihilocreatio:item_pebble>, 0.7);
Sieve.addDiamondMeshRecipe(<ezwastelands:ezwastelandblock>, <exnihilocreatio:item_pebble>, 0.5);
Sieve.addDiamondMeshRecipe(<ezwastelands:ezwastelandblock>, <exnihilocreatio:item_pebble>, 0.2);

mods.exnihilocreatio.Hammer.addRecipe(<ezwastelands:ezwastelandblock>, <minecraft:sand>, 0, 0.4, 0.5);
mods.exnihilocreatio.Hammer.addRecipe(<immersivewastelands:flint_block>, <minecraft:gravel>, 0, 1, 0.5);

Sieve.addStringMeshRecipe(<minecraft:dirt:1>, <minecraft:dirt>, 0.4);

furnace.addRecipe(<minecraft:dirt:1>, <immersivewastelands:flint_block>);

 recipes.addShaped(<minecraft:hopper>,
 [[<ore:ingotLead>,null,<ore:ingotLead>],
  [<ore:ingotLead>,<minecraft:chest>,<ore:ingotLead>],
  [null,<ore:ingotLead>,null]]);
  
