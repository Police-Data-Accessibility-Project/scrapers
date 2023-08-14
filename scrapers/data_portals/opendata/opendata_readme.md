

The opendata scraper expects 3 arguments, which are provided in the template.

The optional argument of `save_subfolder` (defaults to `False`), allows you to save multiple files under one parent dataset folder. To achieve this, you will need to add the folder you want to be the parent folder before the entry in the `save_table`.

For example, if you wanted to save `intersections` in the folder `firearm_intake`, you would simply add `firearm_intake/` to the beginning of the string. `intersections/` would thus become `firearm_intake/intersections/`. As long as your path includes more than one slash, and `save_subfolder` is set to `True`, the scraper will save the files in the subfolder.
