import crafttweaker.oredict.IOreDictEntry;
import crafttweaker.oredict.IOreDict;
import mods.immersiveengineering.MetalPress;
import mods.immersiveengineering.Mixer;
import mods.immersiveengineering.Refinery;
import mods.immersiveengineering.Crusher;

mods.immersiveengineering.MetalPress.addRecipe(<galacticraftcore:basic_item:6>, <ore:ingotCopper>, <immersiveengineering:sheetmetal:8>, 2000);
mods.immersiveengineering.MetalPress.addRecipe(<galacticraftcore:basic_item:7>, <ore:ingotTin>, <immersiveengineering:sheetmetal:8>, 2000);
mods.immersiveengineering.MetalPress.addRecipe(<galacticraftcore:basic_item:8>, <ore:ingotAluminium>, <immersiveengineering:sheetmetal:8>, 2000);
mods.immersiveengineering.MetalPress.addRecipe(<galacticraftcore:basic_item:9>, <ore:ingotSteel>, <immersiveengineering:sheetmetal:8>, 2000);
mods.immersiveengineering.MetalPress.addRecipe(<galacticraftcore:basic_item:11>, <ore:ingotIron>, <immersiveengineering:sheetmetal:8>, 2000);
mods.immersiveengineering.MetalPress.addRecipe(<galacticraftcore:item_basic_moon:1>, <ore:ingotMeteoricIron>, <immersiveengineering:sheetmetal:8>, 2000);
mods.immersiveengineering.MetalPress.addRecipe(<galacticraftplanets:item_basic_mars:5>, <ore:ingotDesh>, <immersiveengineering:sheetmetal:8>, 2000);

mods.immersiveengineering.Crusher.addRecipe(<exnihilocreatio:block_dust>, <minecraft:sand>, 2048);

mods.immersiveengineering.Mixer.addRecipe(<liquid:carbon_colloid>*1000, <liquid:plantoil>*800, [<ore:dustCoke>, <ore:dustCoke>, <ore:dustCoke>, <ore:dustCoke>], 2048);

mods.immersivepetroleum.Distillation.addRecipe([<liquid:gasoline>*11, <liquid:diesel>*6, <liquid:lubricant>*4], [<immersiveengineering:material:7>, <immersiveengineering:material:7>], <liquid:carbon_colloid>*25, 2048, 1, [0.01, 0.033,]);

mods.immersiveengineering.Refinery.addRecipe(<liquid:fuel>*16, <liquid:gasoline>*10, <liquid:ethanol>*6, 2048);

 recipes.addShaped(<immersiveengineering:material:5>,
 [[<minecraft:paper>,<minecraft:paper>,<minecraft:paper>],
  [<minecraft:paper>,<minecraft:stick>,<minecraft:paper>],
  [<minecraft:paper>,<minecraft:paper>,<minecraft:paper>]]);