# RecipeNLG: A Cooking Recipes Dataset
RecipeNLG: A Cooking Recipes Dataset for Semi-Structured Text Generation - Lite version

The dataset contains `7,198` cooking recipes (`>7K`). 
It's processed in more careful way and provides more samples than any other dataset in the area.

## How to use

```bash
pip install git+https://github.com/huggingface/datasets.git
```

Load `m3hrdadfi/recipe_nlg_lite` dataset using `load_dataset`:

```python 
from datasets import load_dataset


dataset = load_dataset("m3hrdadfi/recipe_nlg_lite")
print(dataset)
```

Output:
```text
DatasetDict({
    train: Dataset({
        features: ['uid', 'name', 'description', 'link', 'ner', 'ingredients', 'steps'],
        num_rows: 6118
    })
    test: Dataset({
        features: ['uid', 'name', 'description', 'link', 'ner', 'ingredients', 'steps'],
        num_rows: 1080
    })
})
```

## Examples

```json
{
  "description": "we all know how satisfying it is to make great pork tenderloin, ribs, or a roast but the end of the meal creates a new quandary what do you do with the leftover pork contrary to what you might think, it's not that difficult . how to repurpose your meal is where real cooking creativity comes into play, so let us present to you our favorite pork chop soup recipe . with this recipe, you'll discover how the natural bold flavor of pork gives this hearty soup a lift that a vegetable soup or chicken noodle soup just can't get . it's a dinner recipe to warm you up on a cold winter night or a midday restorative for a long work week . throw all the ingredients in a large pot and let it simmer on the stove for a couple hours, or turn it into a slow cooker recipe and let it percolate for an afternoon . this foolproof recipe transforms your favorite comfort food into an easy meal to warm you up again and again . the health benefits of pork pork is a great option if you're on a low carb diet or trying to up your protein intake . the protein percentage of leaner cuts of pork can be as high as 89 percent pork also provides valuable vitamins and minerals that make pork recipes worthy endeavors . pork has high levels of thiamin and niacin, which other types of meat like beef and lamb lack . they are both b vitamins that aid in several body functions such as metabolism and cell function . pork also delivers a healthy amount of zinc, which aids in brain and immune system function . that makes digging into this pork chop noodle soup all the more alluring . recipe variations this pork soup recipe can be adapted to many diets . if you're following a low carb or ketogenic diet, you can modify the recipe to suit you by leaving out the noodles . if you like, you can add a little crunch by topping it with french fried onions . for cheese lovers, a sprinkle of parmesan cheese can give the soup more body and extra umami flavors . if you're not a noodle lover, this soup recipe works equally well as a potato soup with diced potatoes . if you want to make a southwestern or mexican version, add a can of diced tomatoes and bell peppers for a little extra depth . if you have a penchant for spicy soups, add a little chili powder or red pepper flakes . it's up to you this recipe is great for using up leftover pork chops, but you can make this soup using fresh chops however you decide to do it, you won't be disappointed.",
  "ingredients": "3.0 bone in pork chops, salt, pepper, 2.0 tablespoon vegetable oil, 2.0 cup chicken broth, 4.0 cup vegetable broth, 1.0 red onion, 4.0 carrots, 2.0 clove garlic, 1.0 teaspoon dried thyme, 0.5 teaspoon dried basil, 1.0 cup rotini pasta, 2.0 stalk celery",
  "link": "https://www.yummly.com/private/recipe/Pork-Chop-Noodle-Soup-2249011?layout=prep-steps",
  "name": "pork chop noodle soup",
  "ner": "bone in pork chops, salt, pepper, vegetable oil, chicken broth, vegetable broth, red onion, carrots, garlic, dried thyme, dried basil, rotini pasta, celery",
  "steps": "season pork chops with salt and pepper . heat oil in a dutch oven over medium high heat . add chops and cook for about 4 minutes, until golden brown . flip and cook 4 minutes more, until golden brown . transfer chops to a plate and set aside . pour half of chicken broth into pot, scraping all browned bits from bottom . add remaining chicken broth, vegetable broth, onion, carrots, celery and garlic . mix well and bring to a simmer . add 1 quart water, thyme, basil, 2 teaspoons salt and 1 teaspoon pepper . mix well and bring to a simmer . add chops back to pot and return to simmer . reduce heat and simmer for 90 minutes, stirring occasionally, being careful not to break up chops . transfer chops to plate, trying not to break them up . set aside to cool . raise the heat and bring the soup to a boil . add pasta and cook for about 12 minutes, until tender . when the chops are cool, pull them apart, discarding all the bones and fat . add the meat back to soup and stir well . taste for salt and pepper, and add if needed, before serving.",
  "uid": "dab8b7d0-e0f6-4bb0-aed9-346e80dace1f"
}
```

## Citation

```bibtex
@misc{RecipeNLGLite, 
  author          = {Mehrdad Farahani},
  title           = {RecipeNLG: A Cooking Recipes Dataset for Semi-Structured Text Generation (Lite)},
  year            = 2021,
  publisher       = {GitHub},
  journal         = {GitHub repository},
  howpublished    = {url{https://github.com/m3hrdadfi/recipe-nlg-lite}},
} 
```
