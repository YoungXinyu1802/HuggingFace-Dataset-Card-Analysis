---
license: cc-by-4.0
---
# Galaxy Zoo DECaLS: Detailed Visual Morphology Measurements from Volunteers and Deep Learning for 314,000 Galaxies
- https://github.com/mwalmsley/zoobot
- https://zenodo.org/record/4573248

# Dataset Schema
This schema describes the columns in the GZ DECaLS catalogues; `gz_decals_auto_posteriors`, `gz_decals_volunteers_1_and_2`, and `gz_decals_volunteers_5`.

In all catalogues, galaxies are identified by their `iauname`. Galaxies are unique within a catalogue. `gz_decals_auto_posteriors` contains all galaxies with appropriate imaging and photometry in DECaLS DR5, while `gz_decals_volunteers_1_and_2`, and `gz_decals_volunteers_5` contain subsets classified by volunteers in the respective campaigns.

The columns reporting morphology measurements are named like `{some-question}_{an-answer}`. For example, for the first question, both volunteer catalogues include the following:

| Column      | Description |
| ----------- | ----------- |
| smooth-or-featured_total   | Total number of volunteers who answered the "Smooth of Featured" question     |
| smooth-or-featured_smooth      | Count of volunteers who responded "Smooth" to the "Smooth or Featured" question       |
| smooth-or-featured_featured-or-disk   | Count of volunteers who responded "Featured or Disk", similarly        |
| smooth-or-featured_artifact      | Count of volunteers who responded "Artifact", similarly       |
| smooth-or-featured_smooth_fraction      | Fraction of volunteers who responded "Smooth" to the "Smooth or Featured" question, out of all respondes (i.e. smooth count / total)       |
| smooth-or-featured_featured-or-disk_fraction   | Fraction of volunteers who responded "Featured or Disk", similarly        |
| smooth-or-featured_artifact_fraction      | Fraction of volunteers who responded "Artifact", similarly       |

The questions and answers are slightly different for `gz_decals_volunteers_1_and_2` than `gz_decals_volunteers_5`. See the paper for more.

The volunteer catalogues include `{question}_{answer}_debiased` columns which attempt to estimate what the vote fractions would be if the same galaxy were imaged at lower redshift. See the paper for more. Note that the debiased measurements are highly uncertain on an individual galaxy basis and therefore should be used with caution. Debiased estimates are only available for galaxies with 0.02<z<0.15, -21.5>M_r>-23, and at least 30 votes for the first question (`Smooth or Featured') after volunteer weighting.

The automated catalogue, `gz_decals_auto_posteriors`, includes predictions for all galaxies and all questions even when that question may not be appropriate (e.g. number of spiral arms for a smooth elliptical). To assess relevance, we include `{question}_proportion_volunteers_asked` columns showing the estimated fraction of volunteers that would have been asked each question (i.e. the product of the vote fractions for the preceding answers). We suggest a cut of `{question}_proportion_volunteers_asked` > 0.5 as a starting point. 

The automated catalogue does not include volunteer counts or totals (naturally).

Each catalogue includes a pair of columns to warn where galaxies may have been classified using an inappropriately large field-of-view (due to incorrect radii measurements in the NSA, on which the field-of-view is calculated). We suggest excluding galaxies (<1%) with such warnings.

| Column      | Description |
| ----------- | ----------- |
| wrong_size_statistic      | Mean distance from center of all pixels above double the 20th percentile (i.e. probable source pixels)      |
| wrong_size_warning   | True if wrong_size_statistic > 161.0, our suggested starting cut. Approximately the mean distance of all pixels from center|

For convenience, each catalogue includes the same set of basic astrophysical measurements copied from the NASA Sloan Atlas (NSA). Additional measurements can be added my crossmatching on `iauname` with the NSA. See [here](https://data.sdss.org/datamodel/files/ATLAS_DATA/ATLAS_MAJOR_VERSION/nsa.html) for the NSA schema. If you use these columns, you should cite the NSA.

| Column      | Description |
| ----------- | ----------- |
| ra      | Right ascension (degrees)       |
| dec   | Declination (degrees)        |
| iauname      | Unique identifier listed in NSA v1.0.1 |
| petro_theta   | "Azimuthally-averaged SDSS-style Petrosian radius (derived from r band"        |
| petro_th50      | "Azimuthally-averaged SDSS-style 50% light radius (r-band)"       |
| petro_th90   | "Azimuthally-averaged SDSS-style 50% light radius (r-band)"         |
| elpetro_absmag_r      | "Absolute magnitude from elliptical Petrosian fluxes in rest-frame" in SDSS r |
| sersic_nmgy_r   | "Galactic-extinction corrected AB flux" in SDSS r |
| redshift      | "Heliocentric redshift" ("z" column in NSA) |
| mag_r   | 22.5 - 2.5 log10(sersic_nmgy_r). *Not* the same as the NSA mag column! |

```
@dataset{walmsley_mike_2020_4573248,
  author       = {Walmsley, Mike and
                  Lintott, Chris and
                  Tobias, Geron and
                  Kruk, Sandor J and
                  Krawczyk, Coleman and
                  Willett, Kyle and
                  Bamford, Steven and
                  Kelvin, Lee S and
                  Fortson, Lucy and
                  Gal, Yarin and
                  Keel, William and
                  Masters, Karen and
                  Mehta, Vihang and
                  Simmons, Brooke and
                  Smethurst, Rebecca J and
                  Smith, Lewis and
                  Baeten, Elisabeth M L and
                  Macmillan, Christine},
  title        = {{Galaxy Zoo DECaLS: Detailed Visual Morphology 
                   Measurements from Volunteers and Deep Learning for
                   314,000 Galaxies}},
  month        = dec,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {0.0.2},
  doi          = {10.5281/zenodo.4573248},
  url          = {https://doi.org/10.5281/zenodo.4573248}
}
```