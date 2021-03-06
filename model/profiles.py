from pyldapi.profile import Profile
from pyldapi.renderer import Renderer
from rdflib import Namespace
CATPREZ = Namespace("https://w3id.org/profile/catprez/")


# profile_ckan = Profile(
#     "https://ckan.org/",
#     "CKAN",
#     comment="The Comprehensive Knowledge Archive Network (CKAN) is a web-based open-source management system for "
#     "the storage and distribution of open data. This profile it it's native data model",
#     mediatypes=["application/json"],
#     default_mediatype="application/json",
#     languages=["en"],
#     default_language="en",
# )

profile_dcat = Profile(
    "https://www.w3.org/TR/vocab-dcat/",
    label="DCAT",
    comment="Dataset Catalogue Vocabulary (DCAT) is a W3C-authored RDF vocabulary designed to "
    "facilitate interoperability between data catalogs "
    "published on the Web.",
    mediatypes=["text/html"] + Renderer.RDF_MEDIA_TYPES,
    default_mediatype="text/html",
    languages=["en"],  # default 'en' only for now
    default_language="en",
)

profile_sdo = Profile(
    "https://schema.org",
    label="schema.org",
    comment="Schema.org is a collaborative, community activity with a mission to create, maintain, and promote schemas "
            "for structured data on the Internet, on web pages, in email messages, and beyond.",
    mediatypes=["text/html"] + Renderer.RDF_MEDIA_TYPES,
    default_mediatype="text/html",
    languages=["en"],  # default 'en' only for now
    default_language="en",
)

profile_slist = Profile(
    "https://w3id.org/profile/slist",
    label="Catalogue Simple List",
    comment="A simple JSON object containing basic catalogue metadata and a list of the Resources it contains. "
            "A filterClass query string argument indicating an RDFS/OWL class may be used to filter catalogue members "
            "by type",
    mediatypes=["application/json"],
    default_mediatype="application/json",
    languages=["en"],  # default 'en' only for now
    default_language="en",
)

profile_prof = Profile(
    "https://www.w3.org/TR/dx-prof/",
    label="Profiles Vocabulary",
    comment="The Profiles Vocabulary is an RDF vocabulary created to allow the machine-readable description of "
            "profiles of specifications for information resources.",
    mediatypes=["text/html"] + Renderer.RDF_MEDIA_TYPES,
    default_mediatype="text/html",
    languages=["en"],  # default 'en' only for now
    default_language="en",
)
