#!/usr/bin/env python3
"""Generate the Helalune storefront as static HTML and the bag totals stylesheet."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent

ICON_MENU = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>'
ICON_SEARCH = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M16 16l4 4" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>'
ICON_USER = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="3" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M5 19c1.5-3 3.8-4.5 7-4.5S17.5 16 19 19" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>'
ICON_BAG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.5 8h11l-.8 12H7.3L6.5 8z" fill="none" stroke="currentColor" stroke-width="1.2"/><path d="M9 8V7a3 3 0 0 1 6 0v1" fill="none" stroke="currentColor" stroke-width="1.2"/></svg>'

NAV = [
    ("home", "Home", "index.html"),
    ("shop", "Shop", "shop.html"),
    ("makeup", "Makeup", "shop.html#view-makeup"),
    ("skincare", "Skincare", "shop.html#view-skincare"),
    ("jewelry", "Jewelry", "shop.html#view-jewelry"),
    ("tools", "Tools", "shop.html#view-tools"),
    ("journal", "Journal", "journal.html"),
    ("about", "Atelier", "about.html"),
]

PRODUCTS = [
    {
        "slug": "luminous-veil",
        "name": "Luminous Veil Foundation",
        "cat": "makeup",
        "cats": ["makeup"],
        "cat_label": "Makeup",
        "price": 54,
        "eyebrow": "Complexion",
        "volume": "30 ml",
        "image": "luxury.png",
        "positions": ["50% 78%", "22% 70%", "78% 62%"],
        "blurb": "A sheer veil that evens tone and leaves skin looking like skin, only rested.",
        "story": "Pressed in a warm nude light, Luminous Veil sits close to the skin. It softens redness and shadows without a mask, then wears through a long day or a long evening.",
        "use": "Warm a small amount between the fingers. Press it over moisturised skin from the centre of the face outward. Build only where the light needs help.",
        "ingredients": "Aqua, squalane, glycerin, caprylic/capric triglyceride, silica, titanium dioxide, iron oxides, tocopherol.",
        "shades": [("Porcelain", "#f3e2d4"), ("Sand", "#e3c2a2"), ("Honey", "#c89060"), ("Amber", "#8a5638")],
        "default": True,
    },
    {
        "slug": "nude-couture-lip",
        "name": "Nude Couture Lipstick",
        "cat": "makeup",
        "cats": ["makeup"],
        "cat_label": "Makeup",
        "price": 32,
        "eyebrow": "Color",
        "volume": "3.5 g",
        "image": "storefront.png",
        "positions": ["18% 28%", "82% 18%", "50% 88%"],
        "blurb": "A satin nude with the depth of a couture lining, not a flat beige.",
        "story": "The bullet is cut square, like the rest of the maison. Color melts on contact and stays inside the lip line, from a quiet nude to a soft brick.",
        "use": "Line with the edge of the bullet, then fill. Blot once if you want a stain rather than a satin finish.",
        "ingredients": "Ricinus communis seed oil, cera alba, caprylic/capric triglyceride, mica, iron oxides, tocopherol.",
        "shades": [("Nude", "#c98978"), ("Rose", "#b85d62"), ("Brick", "#8e3d38")],
        "default": False,
    },
    {
        "slug": "atelier-blush",
        "name": "Atelier Blush",
        "cat": "makeup",
        "cats": ["makeup"],
        "cat_label": "Makeup",
        "price": 38,
        "eyebrow": "Color",
        "volume": "6 g",
        "image": "storefront.png",
        "positions": ["48% 62%", "22% 62%", "70% 40%"],
        "blurb": "Powdered flush, the color of skin after a walk, pressed into a sharp compact.",
        "story": "Atelier Blush is a whisper of terracotta and rose. It is meant to be seen as health, not as a circle of pigment.",
        "use": "Tap a small brush through the pan. Sweep from the cheekbone toward the temple. Stop before you think you should.",
        "ingredients": "Mica, talc, magnesium stearate, silica, iron oxides, tin oxide.",
        "shades": [("Veil", "#e7b7a8"), ("Flush", "#d4898a"), ("Clay", "#c47a62")],
        "default": False,
    },
    {
        "slug": "dew-serum",
        "name": "Hyaluronic Dew Serum",
        "cat": "skincare",
        "cats": ["skincare", "everyday"],
        "cat_label": "Skincare",
        "price": 42,
        "eyebrow": "Treat",
        "volume": "30 ml",
        "image": "glow.png",
        "positions": ["48% 42%", "62% 18%", "40% 70%"],
        "blurb": "A watery serum that pulls moisture in and leaves a quiet glass on the skin.",
        "story": "Dew Serum is the middle of the everyday glow: after cleansing, before the veil of moisture. Hyaluronic acid and vitamin C brighten without sting.",
        "use": "Press four drops over damp skin, morning and night. Follow with moisture while the serum is still wet.",
        "ingredients": "Aqua, sodium hyaluronate, glycerin, 3-O-ethyl ascorbic acid, panthenol, allantoin.",
        "shades": [],
        "default": True,
    },
    {
        "slug": "foaming-cleanse",
        "name": "Everyday Foaming Cleanse",
        "cat": "skincare",
        "cats": ["skincare", "everyday"],
        "cat_label": "Skincare",
        "price": 28,
        "eyebrow": "Cleanse",
        "volume": "150 ml",
        "image": "glow.png",
        "positions": ["30% 28%", "18% 55%", "55% 20%"],
        "blurb": "A low, cushiony foam that lifts the day and leaves the skin comfortable.",
        "story": "The first step of the glow edit. It removes sunscreen, powder, and city film without the tight feeling of a harsh wash.",
        "use": "Massage a walnut of foam over a wet face for thirty seconds. Rinse with lukewarm water.",
        "ingredients": "Aqua, glycerin, cocamidopropyl betaine, sodium cocoyl isethionate, panthenol, aloe barbadensis leaf juice.",
        "shades": [],
        "default": False,
    },
    {
        "slug": "moisture-veil",
        "name": "Day & Night Moisture",
        "cat": "skincare",
        "cats": ["skincare", "everyday"],
        "cat_label": "Skincare",
        "price": 36,
        "eyebrow": "Seal",
        "volume": "50 ml",
        "image": "glow.png",
        "positions": ["70% 30%", "78% 55%", "60% 18%"],
        "blurb": "A light cream that seals the serum and sits well under foundation.",
        "story": "Moisture Veil is the last step of care and the first kindness under makeup. It is rich enough for the evening and thin enough for noon.",
        "use": "Warm a pea of cream between the palms. Press it over serum. In the day, give it a minute before Luminous Veil.",
        "ingredients": "Aqua, squalane, glycerin, butyrospermum parkii butter, niacinamide, ceramide NP, tocopherol.",
        "shades": [],
        "default": False,
    },
    {
        "slug": "powder-brush",
        "name": "Atelier Powder Brush",
        "cat": "tools",
        "cats": ["tools"],
        "cat_label": "Tools",
        "price": 34,
        "eyebrow": "Tools",
        "volume": "One size",
        "image": "tools.png",
        "positions": ["62% 78%", "30% 72%", "80% 60%"],
        "blurb": "A full, soft head for powder and blush, with a weighted handle that stays quiet in the hand.",
        "story": "Care, in the hand. The brush is cut for pressed powder and Atelier Blush, dense enough to place color and soft enough not to scratch.",
        "use": "Swirl once in the pan, tap the ferrule, then sweep. Wash the head weekly with a gentle soap and dry it flat.",
        "ingredients": "Synthetic hair, aluminium ferrule, lacquered handle.",
        "shades": [],
        "default": False,
    },
    {
        "slug": "cloud-sponge",
        "name": "Cloud Sponge",
        "cat": "tools",
        "cats": ["tools"],
        "cat_label": "Tools",
        "price": 14,
        "eyebrow": "Tools",
        "volume": "One sponge",
        "image": "tools.png",
        "positions": ["18% 48%", "24% 58%", "12% 40%"],
        "blurb": "A firm, pointed sponge for pressing foundation into a second-skin finish.",
        "story": "Used damp, the sponge sheers Luminous Veil. Used dry, it lifts extra powder from the centre of the face.",
        "use": "Wet, squeeze until it is damp, not dripping, then bounce. Rinse after each use and replace when the edge frays.",
        "ingredients": "Non-latex foam.",
        "shades": [],
        "default": False,
    },
    {
        "slug": "gilded-hoops",
        "name": "Gilded Hoop Earrings",
        "cat": "jewelry",
        "cats": ["jewelry"],
        "cat_label": "Jewelry",
        "price": 48,
        "eyebrow": "Jewelry",
        "volume": "Pair",
        "image": "jewelry.png",
        "positions": ["50% 42%", "30% 30%", "70% 55%"],
        "blurb": "Gold-tone hoops, light enough for every day and bright enough for the evening edit.",
        "story": "Sara's edit pairs imitation jewelry with complexion color. These hoops are gold-tone, not solid gold: a clean circle meant to sit beside a nude lip.",
        "use": "Latch the hinge closed. Wipe with a soft cloth after wear. Keep the pair dry.",
        "ingredients": "Gold-tone plated brass. Imitation jewelry.",
        "shades": [("Gold-tone", "#c6a15b"), ("Champagne", "#d8c3a0")],
        "default": True,
    },
    {
        "slug": "champagne-cuff",
        "name": "Champagne Cuff",
        "cat": "jewelry",
        "cats": ["jewelry"],
        "cat_label": "Jewelry",
        "price": 55,
        "eyebrow": "Jewelry",
        "volume": "One cuff",
        "image": "jewelry.png",
        "positions": ["40% 70%", "60% 28%", "48% 48%"],
        "blurb": "An open cuff in champagne metal, wide enough to read as jewelry and light enough to forget.",
        "story": "Worn alone, over a bare wrist, with Atelier Blush still visible. The metal is an imitation finish, polished, not precious.",
        "use": "Slide on from the side. Avoid water, perfume, and sleep. Store it flat in the pouch.",
        "ingredients": "Champagne-tone or silver-tone plated alloy. Imitation jewelry.",
        "shades": [("Champagne", "#d9c7a4"), ("Silver-tone", "#d5d3d0")],
        "default": False,
    },
]


def money(amount):
    return f"${amount}"


def ship_label(merch):
    if merch <= 0:
        return "—"
    if merch >= 120:
        return "Complimentary"
    return "$8"


def quote_totals(mask, promo):
    chosen = [p for i, p in enumerate(PRODUCTS) if mask & (1 << i)]
    merch = sum(p["price"] for p in chosen)
    discount = int(round(merch * 0.10)) if promo and merch else 0
    ship = 0 if merch == 0 or merch >= 120 else 8
    due = merch - discount + ship
    return chosen, merch, discount, ship, due


def totals_css():
    rules = [
        "/* Generated by build_site.py. Totals for every bag combination. */",
        ".sum { display: none; }",
    ]
    n = len(PRODUCTS)
    for i, _p in enumerate(PRODUCTS):
        rules.append(f"#p{i}:checked ~ .layout .line-{i} .boxface::after {{ opacity: 1; }}")
        rules.append(f"#p{i}:checked ~ .layout .line-{i} .on {{ display: inline; }}")
        rules.append(f"#p{i}:not(:checked) ~ .layout .line-{i} .off {{ display: inline; }}")
        rules.append(f"#p{i}:not(:checked) ~ .layout .line-{i} {{ opacity: 0.55; }}")
    rules.append("#promo:checked ~ .layout .promo-row .boxface::after { opacity: 1; }")
    rules.append(".bag:not(:has(.pick:checked)) .checkout-fields { display: none; }")
    rules.append(".bag:not(:has(.pick:checked)) .promo-row { display: none; }")
    for mask in range(1 << n):
        for promo in (False, True):
            parts = []
            for i in range(n):
                state = "checked" if mask & (1 << i) else "not(:checked)"
                parts.append(f"#p{i}:{state}")
            parts.append("#promo:checked" if promo else "#promo:not(:checked)")
            cls = f"s-{mask}-{'p' if promo else 'f'}"
            selector = " ~ ".join(parts) + f" ~ .layout .{cls}"
            rules.append(f"{selector} {{ display: block; }}")
    return "\n".join(rules) + "\n"


def sum_blocks():
    blocks = []
    n = len(PRODUCTS)
    for mask in range(1 << n):
        for promo in (False, True):
            chosen, merch, discount, ship, due = quote_totals(mask, promo)
            cls = f"s-{mask}-{'p' if promo else 'f'}"
            if not chosen:
                body = (
                    "<p>Your bag is empty.</p>"
                    '<p class="fine">Tick a piece. The due amount updates on this page.</p>'
                    '<p><a class="link" href="shop.html">Shop the edit</a></p>'
                )
            else:
                items = "".join(
                    f"<li>{escape(p['name'])} — {money(p['price'])}</li>" for p in chosen
                )
                promo_line = f"<p>HELALUNE10 −{money(discount)}</p>" if promo else ""
                body = (
                    f'<p class="fine">{len(chosen)} piece{"s" if len(chosen) != 1 else ""}</p>'
                    f"<ul>{items}</ul>"
                    f"<p>Merchandise <span class=\"price\">{money(merch)}</span></p>"
                    f"{promo_line}"
                    f"<p>Shipping {escape(ship_label(merch))}</p>"
                    f'<p class="due price">{money(due)}</p>'
                )
            blocks.append(f'<div class="sum {cls}">{body}</div>')
    return "\n".join(blocks)


def img(src, alt, position=None, width=736, height=1104):
    style = f' style="object-position:{position}"' if position else ""
    return (
        f'<img src="assets/{src}" alt="{escape(alt)}" width="{width}" height="{height}"{style}>'
    )


def card(product):
    classes = " ".join(["card", *product["cats"]])
    return f"""
<article class="{classes}">
  <div class="media">
    <a href="product-{product['slug']}.html">{img(product['image'], product['name'], product['positions'][0])}</a>
    <a class="quick" href="cart.html#piece-{product['slug']}">Add to bag</a>
  </div>
  <div class="meta">
    <p class="eyebrow">{escape(product['eyebrow'])}</p>
    <h3><a href="product-{product['slug']}.html">{escape(product['name'])}</a></h3>
    <p class="price">{money(product['price'])}</p>
  </div>
</article>""".strip()


def cards_for(cat=None):
    chosen = [p for p in PRODUCTS if cat is None or cat in p["cats"]]
    return "\n".join(card(p) for p in chosen)


def index_groups():
    groups = []
    for key, label in (("makeup", "Makeup"), ("skincare", "Skincare"), ("tools", "Tools"), ("jewelry", "Jewelry")):
        links = "\n".join(
            f'<a href="product-{p["slug"]}.html">{escape(p["name"])}</a>'
            for p in PRODUCTS
            if p["cat"] == key
        )
        groups.append(f'<div><p class="eyebrow">{label}</p>{links}</div>')
    return "\n".join(groups)


def shell(title, current, body, description, extra_css=""):
    nav = []
    for key, label, href in NAV:
        current_attr = ' aria-current="page"' if key == current else ""
        nav.append(f'<a href="{href}"{current_attr}>{label}</a>')
    nav_html = "\n".join(nav)
    panel_links = "\n".join(f"<li>{item}</li>" for item in nav)
    year = "2026"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <meta name="theme-color" content="#faf7f5">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;0,6..96,600;1,6..96,400&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
  {extra_css}
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>
  <input class="state" type="radio" name="panel" id="panel-none" checked>
  <input class="state" type="radio" name="panel" id="panel-nav">
  <input class="state" type="radio" name="panel" id="panel-search">
  <input class="state" type="radio" name="panel" id="panel-bag">
  <p class="promo">Complimentary shipping on orders over $120 · Code HELALUNE10</p>
  <header class="header">
    <a class="logo" href="index.html"><span class="logo-mark">H</span><span class="logo-word">Helalune</span></a>
    <nav class="nav-desktop" aria-label="Primary">{nav_html}</nav>
    <div class="header-actions">
      <label class="icon-btn menu-btn" for="panel-nav" aria-label="Open menu">{ICON_MENU}</label>
      <label class="icon-btn" for="panel-search" aria-label="Open index">{ICON_SEARCH}</label>
      <a class="icon-btn" href="account.html" aria-label="Account">{ICON_USER}</a>
      <label class="icon-btn" for="panel-bag" aria-label="Open bag">{ICON_BAG}</label>
    </div>
  </header>
  <div class="panel panel-nav">
    <div class="panel-top"><p class="eyebrow">Menu</p><label class="link" for="panel-none">Close</label></div>
    <ul>{panel_links}</ul>
  </div>
  <div class="panel panel-search">
    <div class="wrap">
      <div class="panel-top"><p class="eyebrow">Index</p><label class="link" for="panel-none">Close</label></div>
      <h2>Find a piece.</h2>
      <div class="index-grid">{index_groups()}</div>
    </div>
  </div>
  <aside class="panel panel-bag">
    <div class="panel-top"><p class="eyebrow">Bag</p><label class="link" for="panel-none">Close</label></div>
    <h2>The edit, ticked by you.</h2>
    <p class="lede">Pieces stay on the bag page. Tick what you want, apply HELALUNE10, and the due amount changes before you place the order.</p>
    <div class="bag-list">
      <p><a href="cart.html">Open the bag</a></p>
      <p><a href="cart.html#checkout">Continue to delivery</a></p>
      <p><a href="shop.html">Return to the edit</a></p>
    </div>
  </aside>
  <label class="scrim" for="panel-none" aria-label="Close"></label>
  <main id="content">
    {body}
  </main>
  <footer class="footer">
    <div class="wrap foot-grid">
      <div>
        <h2>Helalune</h2>
        <p>Haute nude couture for complexion, care, tools, and imitation jewelry. Edited in quiet light.</p>
      </div>
      <div>
        <p class="eyebrow">Maison</p>
        <a href="about.html">The atelier</a>
        <a href="journal.html">Journal</a>
        <a href="account.html">Account</a>
        <a href="contact.html">Write to us</a>
      </div>
      <div>
        <p class="eyebrow">Care</p>
        <a href="shipping.html">Shipping</a>
        <a href="returns.html">Returns</a>
        <a href="faq.html">Questions</a>
        <a href="cart.html">Your bag</a>
      </div>
      <div>
        <p class="eyebrow">Write</p>
        <a href="contact.html">Contact</a>
        <a href="mailto:hello@helalune.com">hello@helalune.com</a>
      </div>
    </div>
    <div class="wrap legal">
      <span>© {year} Helalune. Imitation jewelry is gold-tone, not fine gold.</span>
      <a href="privacy.html">Privacy</a>
    </div>
  </footer>
</body>
</html>
"""


def page_home():
    makeup = "\n".join(card(p) for p in PRODUCTS if p["cat"] == "makeup")
    tools = "\n".join(card(p) for p in PRODUCTS if p["cat"] == "tools")
    everyday = "\n".join(card(p) for p in PRODUCTS if "everyday" in p["cats"])
    jewelry = "\n".join(card(p) for p in PRODUCTS if p["cat"] == "jewelry")
    skincare = "\n".join(card(p) for p in PRODUCTS if p["cat"] == "skincare")
    body = f"""
<section class="hero">
  <figure class="hero-media">{img("luxury.png", "Helalune complexion and color arranged on white plinths", "50% 70%")}</figure>
  <div class="hero-copy">
    <p class="eyebrow">01 — Luxury cosmetics</p>
    <h1>The collection, composed in nude light.</h1>
    <p class="lede">Helalune edits complexion, color, care, and couture objects with the calm of an atelier. Ten pieces. Nothing extra.</p>
    <div class="hero-actions">
      <a class="btn" href="shop.html#view-makeup">Shop makeup</a>
      <a class="btn btn-ghost" href="about.html">The maison</a>
    </div>
    <dl class="hero-facts">
      <div><dt>Finish</dt><dd>Powdered nude</dd></div>
      <div><dt>Edition</dt><dd>Ten pieces</dd></div>
      <div><dt>Shipping</dt><dd>Free over $120</dd></div>
    </dl>
  </div>
</section>
<section class="chapter-block" id="care">
  <div class="chapter wrap">
    <div>
      <p class="eyebrow">02 — Care your beauty</p>
      <h2>Tools with a steady hand.</h2>
      <p class="lede">Brushes and a sponge, cut for the way the complexion is pressed on, not painted on. Beauty care, kept architectural.</p>
      <p><a class="link" href="shop.html#view-tools">Shop tools</a></p>
    </div>
    <figure>{img("tools.png", "Beauty care tools, lip color, and brushes on a blush ground", "50% 60%")}</figure>
  </div>
  <div class="wrap rail-block"><div class="rail two">{tools}</div></div>
</section>
<section class="chapter-block" id="everyday">
  <div class="chapter wrap flip">
    <div>
      <p class="eyebrow">03 — Your everyday glow, simplified</p>
      <h2>Three steps. Then the day.</h2>
      <p class="lede">Cleanse, treat, seal. The glow edit is short on purpose, so the mirror takes less time than the morning.</p>
      <p><a class="link" href="shop.html#view-everyday">Shop the glow</a></p>
    </div>
    <figure>{img("everyday.png", "Every day essentials floating above a blush shopping basket", "50% 45%", 736, 1008)}</figure>
  </div>
  <div class="wrap rail-block"><div class="rail">{everyday}</div></div>
</section>
<section class="chapter-block" id="jewelry">
  <div class="chapter wrap">
    <div>
      <p class="eyebrow">04 — Sara's edit</p>
      <h2>Imitation jewelry, worn with color.</h2>
      <p class="lede">Gold-tone hoops and a champagne cuff, made to sit beside a nude lip. The metal is plated imitation, chosen for gleam rather than weight.</p>
      <p><a class="link" href="shop.html#view-jewelry">Shop jewelry</a></p>
    </div>
    <figure>{img("jewelry.png", "A pouch of complexion color and gold-tone pieces", "50% 45%")}</figure>
  </div>
  <div class="wrap rail-block"><div class="rail two">{jewelry}</div></div>
</section>
<section class="chapter-block" id="storefront">
  <div class="chapter wrap flip">
    <div>
      <p class="eyebrow">05 — The storefront</p>
      <h2>A new beauty edit, in one room.</h2>
      <p class="lede">Makeup, skincare, tools, and jewelry on one floor. Shop by ritual, or take the whole ten-piece edit.</p>
      <div class="stack-actions">
        <a class="btn" href="shop.html">Enter the shop</a>
        <a class="btn btn-ghost" href="cart.html">Open the bag</a>
      </div>
    </div>
    <figure>{img("storefront.png", "An edited flat lay of complexion and color", "50% 40%")}</figure>
  </div>
  <div class="wrap tiles">
    <a class="tile" href="shop.html#view-makeup"><div class="media">{img("luxury.png", "", "50% 75%")}</div><span>Makeup</span></a>
    <a class="tile" href="shop.html#view-skincare"><div class="media">{img("glow.png", "", "50% 40%", 736, 736)}</div><span>Skincare</span></a>
    <a class="tile" href="shop.html#view-tools"><div class="media">{img("tools.png", "", "50% 70%")}</div><span>Tools</span></a>
    <a class="tile" href="shop.html#view-jewelry"><div class="media">{img("jewelry.png", "", "50% 50%")}</div><span>Jewelry</span></a>
  </div>
</section>
<section class="chapter-block" id="glow">
  <div class="chapter wrap">
    <div>
      <p class="eyebrow">06 — Get your glow on</p>
      <h2>A ritual in nude and rose.</h2>
      <p class="lede">The skincare edit is a pink still life you can actually finish: foam, dew, then a veil of moisture.</p>
      <ol class="steps">
        <li><span>01</span><div><strong>Cleanse</strong><a href="product-foaming-cleanse.html">Everyday Foaming Cleanse</a></div></li>
        <li><span>02</span><div><strong>Treat</strong><a href="product-dew-serum.html">Hyaluronic Dew Serum</a></div></li>
        <li><span>03</span><div><strong>Seal</strong><a href="product-moisture-veil.html">Day &amp; Night Moisture</a></div></li>
      </ol>
    </div>
    <figure>{img("glow.png", "Pink everyday skincare bottles and tubes", "50% 45%", 736, 736)}</figure>
  </div>
  <div class="wrap rail-block"><div class="rail">{skincare}</div></div>
</section>
<section class="wrap quotes">
  <blockquote>The nude is not an absence of color. It is the color of the room.<footer>Atelier note</footer></blockquote>
  <blockquote>Jewelry here is imitation, and it is meant to be worn, not locked away.<footer>Sara's edit</footer></blockquote>
</section>
<section class="wrap salon" id="visit">
  <div>
    <p class="eyebrow">The list</p>
    <h2>Letters, rarely.</h2>
    <p class="lede">New shades and the next edit. No weekly noise.</p>
  </div>
  <div id="news">
    <form class="news" action="#news" method="get">
      <input type="email" required placeholder="Email address" autocomplete="email" aria-label="Email address">
      <button class="btn" type="submit">Join</button>
    </form>
    <p class="joined">You are on the list. We write rarely.</p>
  </div>
</section>
"""
    # makeup variable is used? I built makeup but the hero doesn't show a rail of makeup.
    # Include a makeup rail under the hero so chapter 01 has pieces, not only a photograph.
    makeup_rail = f'<div class="wrap rail-block"><div class="rail">{makeup}</div></div>'
    body = body.replace(
        "</section>\n<section class=\"chapter-block\" id=\"care\">",
        f"</section>\n{makeup_rail}\n<section class=\"chapter-block\" id=\"care\">",
        1,
    )
    return shell(
        "Helalune — Haute nude couture",
        "home",
        body,
        "Helalune is a beauty and fashion edit: makeup, skincare, tools, and imitation jewelry.",
    )


def page_shop():
    counts = {
        "all": len(PRODUCTS),
        "makeup": sum(1 for p in PRODUCTS if "makeup" in p["cats"]),
        "skincare": sum(1 for p in PRODUCTS if "skincare" in p["cats"]),
        "everyday": sum(1 for p in PRODUCTS if "everyday" in p["cats"]),
        "tools": sum(1 for p in PRODUCTS if "tools" in p["cats"]),
        "jewelry": sum(1 for p in PRODUCTS if "jewelry" in p["cats"]),
        "fragrance": 0,
    }
    chips = [
        ("view-all", "All"),
        ("view-makeup", "Makeup"),
        ("view-skincare", "Skincare"),
        ("view-everyday", "Everyday"),
        ("view-tools", "Tools"),
        ("view-jewelry", "Jewelry"),
        ("view-fragrance", "Fragrance"),
    ]
    chip_html = "\n".join(f'<a class="chip" id="{i}" href="#{i}">{label}</a>' for i, label in chips)
    count_html = "\n".join(
        f'<p class="count count-{key}">{counts[key]} piece{"s" if counts[key] != 1 else ""}</p>'
        for key in counts
    )
    body = f"""
<header class="page-head wrap">
  <p class="eyebrow">Shop</p>
  <h1>The edit.</h1>
  <p class="lede">Ten pieces, in the order of the maison: makeup, care, everyday glow, jewelry, then the full storefront.</p>
</header>
<div class="shop wrap">
  {chip_html}
  {count_html}
  <div class="filter-empty">
    <h2>Fragrance is not in this drop.</h2>
    <p class="lede">The next atelier letter will carry it. The complexion edit is ready now.</p>
    <p><a class="link" href="#view-all">Back to all pieces</a></p>
  </div>
  <div class="grid">
    {cards_for()}
  </div>
</div>
"""
    return shell("Shop — Helalune", "shop", body, "Shop the Helalune edit of makeup, skincare, tools, and jewelry.")


def page_product(product):
    shades = product["shades"]
    shade_inputs = ""
    shade_names = ""
    shade_swatches = ""
    if shades:
        bits_in, bits_name, bits_sw = [], [], []
        for i, (name, color) in enumerate(shades, start=1):
            checked = " checked" if i == 1 else ""
            bits_in.append(
                f'<input class="state" type="radio" name="shade" id="s{i}"{checked}>'
            )
            bits_name.append(f'<p class="shade-name n{i}">{escape(name)}</p>')
            bits_sw.append(
                f'<label for="s{i}" title="{escape(name)}"><i style="--sw:{color}"></i></label>'
            )
        shade_inputs = "\n".join(bits_in)
        shade_names = "".join(bits_name)
        shade_swatches = f'<p class="eyebrow">Shade</p>{shade_names}<div class="swatches">{"".join(bits_sw)}</div>'
    frames = []
    thumbs = []
    for i, pos in enumerate(product["positions"], start=1):
        frames.append(f'<div class="frame f{i}">{img(product["image"], product["name"], pos)}</div>')
        thumbs.append(f'<label for="g{i}">{img(product["image"], "", pos)}</label>')
    related = [p for p in PRODUCTS if p["slug"] != product["slug"] and p["cat"] == product["cat"]]
    if len(related) < 2:
        related += [p for p in PRODUCTS if p["slug"] != product["slug"] and p not in related]
    related = related[:3]
    body = f"""
<div class="wrap pdp">
  <input class="state" type="radio" name="gal" id="g1" checked>
  <input class="state" type="radio" name="gal" id="g2">
  <input class="state" type="radio" name="gal" id="g3">
  {shade_inputs}
  <div class="gallery">
    {''.join(frames)}
    <div class="thumbs">{''.join(thumbs)}</div>
  </div>
  <div class="buy">
    <p class="crumb"><a href="shop.html">Shop</a> / <a href="shop.html#view-{product['cat']}">{escape(product['cat_label'])}</a></p>
    <p class="eyebrow">{escape(product['eyebrow'])}</p>
    <h1>{escape(product['name'])}</h1>
    <p class="price">{money(product['price'])} · {escape(product['volume'])}</p>
    <p class="lede">{escape(product['blurb'])}</p>
    {shade_swatches}
    <div class="buy-actions">
      <a class="btn" href="cart.html#piece-{product['slug']}">Add to bag</a>
      <a class="btn btn-ghost" href="cart.html#checkout">Checkout</a>
    </div>
    <details open>
      <summary>Story</summary>
      <p>{escape(product['story'])}</p>
    </details>
    <details>
      <summary>How to use</summary>
      <p>{escape(product['use'])}</p>
    </details>
    <details>
      <summary>Composition</summary>
      <p>{escape(product['ingredients'])}</p>
    </details>
    <details>
      <summary>Shipping and returns</summary>
      <p>Complimentary shipping from $120. Under that, delivery is $8. Pay when the order arrives. Unworn pieces can return within 14 days. See <a href="shipping.html">shipping</a> and <a href="returns.html">returns</a>.</p>
    </details>
  </div>
</div>
<section class="wrap related">
  <h2>Worn with</h2>
  <div class="rail">{''.join(card(p) for p in related)}</div>
</section>
"""
    return shell(
        f"{product['name']} — Helalune",
        "shop",
        body,
        product["blurb"],
    )


def bag_lines():
    rows = []
    for i, p in enumerate(PRODUCTS):
        checked = " checked" if p["default"] else ""
        rows.append(
            f'<input class="pick state" type="checkbox" id="p{i}" name="piece" value="{escape(p["name"])}"{checked}>'
        )
    rows.append('<input class="state" type="checkbox" id="promo" name="code" value="HELALUNE10">')
    lines = []
    for i, p in enumerate(PRODUCTS):
        lines.append(f"""
<article class="line line-{i}" id="piece-{p['slug']}">
  {img(p['image'], "", p['positions'][0])}
  <div>
    <p class="eyebrow">{escape(p['cat_label'])}</p>
    <h2><a href="product-{p['slug']}.html">{escape(p['name'])}</a></h2>
    <p class="price">{money(p['price'])}</p>
    <p class="nudge">This piece is highlighted. Tick the square to keep it in the bag.</p>
  </div>
  <label class="include" for="p{i}"><span class="boxface"></span><span class="on">In bag</span><span class="off">Add</span></label>
</article>""".strip())
    return "\n".join(rows), "\n".join(lines)


def checkout_fields():
    return f"""
<div class="checkout-fields" id="checkout">
  <h2>Delivery</h2>
  <p class="lede">Pay when the order arrives. Nothing you type here is stored, and card numbers are never asked.</p>
  <div class="fields">
    <label class="field"><span>Full name</span><input required autocomplete="name"></label>
    <label class="field"><span>Phone</span><input required autocomplete="tel" inputmode="tel"></label>
    <label class="field wide"><span>Email</span><input type="email" required autocomplete="email"></label>
    <div class="field wide">
      <span>Payment</span>
      <div class="choices">
        <label class="choice"><input class="box" type="radio" name="pay" value="delivery" checked><span>Pay on delivery</span></label>
        <label class="choice"><input class="box" type="radio" name="pay" value="transfer"><span>Bank transfer after we confirm</span></label>
      </div>
    </div>
    <p class="fine pay-note">Helalune does not take a card number on this page. You pay on delivery, or we send transfer details after the order is confirmed on screen.</p>
    <div class="field wide"><button class="btn btn-full" type="submit">Place order</button></div>
  </div>
</div>
"""


def page_bag(mode):
    inputs, lines = bag_lines()
    if mode == "checkout":
        head = """
<header class="page-head wrap">
  <p class="eyebrow">Checkout</p>
  <h1>Place the order.</h1>
  <p class="lede">The bag above is the order. Change a tick and the due amount follows, then leave a name for the order.</p>
</header>"""
        current = "cart"
        title = "Checkout — Helalune"
    else:
        head = """
<header class="page-head wrap">
  <p class="eyebrow">Bag</p>
  <h1>Your bag.</h1>
  <p class="lede">Three pieces begin in the bag: the veil, the serum, and the hoops. Untick them, add others, or use HELALUNE10. The total is calculated on this page.</p>
</header>"""
        title = "Bag — Helalune"
    body = f"""
{head}
<form class="bag wrap bag-page" action="order.html" method="get">
  {inputs}
  <input type="hidden" name="order" value="placed">
  <div class="layout">
    <div class="lines">{lines}</div>
    <aside class="summary">
      <h2>Due</h2>
      {sum_blocks()}
      <label class="promo-row" for="promo"><span class="boxface"></span><span>Apply HELALUNE10 · 10%</span></label>
      <p class="fine">Shipping is complimentary from $120, otherwise $8. One of each piece.</p>
      <p style="margin-top:1rem"><a class="link" href="#checkout">Continue to delivery</a></p>
    </aside>
    {checkout_fields()}
  </div>
</form>
"""
    return shell(title, "cart", body, "Your Helalune bag and delivery details.", extra_css='<link rel="stylesheet" href="css/totals.css">')


def page_order():
    body = """
<section class="wrap confirm">
  <p class="order-no">Order HL-20481</p>
  <h1>It is placed.</h1>
  <p class="lede">The atelier has the shape of your order on this page. No payment was taken. If you chose pay on delivery, it is collected when the order arrives. If you chose a transfer, the next letter would carry the details.</p>
  <p class="fine">This storefront is HTML and CSS only, so the order is confirmed here and is not sent to a server.</p>
  <div class="hero-actions">
    <a class="btn" href="shop.html">Continue shopping</a>
    <a class="btn btn-ghost" href="cart.html">Return to the bag</a>
  </div>
</section>
"""
    return shell("Order confirmed — Helalune", "cart", body, "Your Helalune order is confirmed on this page.")


def page_about():
    body = f"""
<header class="page-head wrap">
  <p class="eyebrow">The maison</p>
  <h1>Haute nude, cut sharp.</h1>
  <p class="lede">Helalune is a small edit of beauty and fashion. The light is warm. The corners are square. The jewelry is imitation and says so.</p>
</header>
<div class="split wrap">
  <figure>{img("luxury.png", "The Helalune complexion edit", "50% 65%")}</figure>
  <div class="prose" style="padding-bottom:0">
    <p>The maison began as a dressing table edited down to what a person actually finishes: a foundation, a lip, a blush, a short ritual for skin, two tools, and two pieces of jewelry that can be worn with all of it.</p>
    <p>We work in nude, bronze, and espresso. Campaign photographs in this edit are the six rooms of the house: luxury cosmetics, care tools, everyday glow, Sara's jewelry, the storefront, and the glow ritual.</p>
  </div>
</div>
<div class="wrap principles">
  <article><h2>Nude light</h2><p>Color stays close to skin. If a shade shouts, it does not ship.</p></article>
  <article><h2>Sharp cut</h2><p>Packaging, type, and trays keep a right angle. Nothing is softened into a pill.</p></article>
  <article><h2>Honest metal</h2><p>Hoops and the cuff are gold-tone imitation. They are made to be worn, not stored as treasure.</p></article>
</div>
"""
    return shell("The atelier — Helalune", "about", body, "The Helalune maison: nude light, sharp cut, honest imitation jewelry.")


def page_journal():
    body = f"""
<header class="page-head wrap">
  <p class="eyebrow">Journal</p>
  <h1>Notes from the edit.</h1>
</header>
<div class="journal-list wrap">
  <article>
    <p class="eyebrow">03</p>
    <div>
      <h2><a class="stretch" href="#everyday-essay">Your everyday glow, simplified</a></h2>
      <p>Why the morning routine stops at three steps.</p>
    </div>
  </article>
  <article>
    <p class="eyebrow">06</p>
    <div>
      <h2><a href="#glow-essay">Get your glow on</a></h2>
      <p>Foam, dew, and a veil, in that order.</p>
    </div>
  </article>
  <article>
    <p class="eyebrow">02</p>
    <div>
      <h2><a href="#tools-essay">Care, in the hand</a></h2>
      <p>The brush and the sponge are part of the formula.</p>
    </div>
  </article>
</div>
<article class="essay wrap" id="everyday-essay">
  <p class="eyebrow">Essay</p>
  <h2>Your everyday glow, simplified.</h2>
  {img("everyday.png", "Everyday essentials", "50% 40%", 736, 1008)}
  <p>A long routine is a way of postponing the day. Helalune keeps the glow to a cleanse, a serum, and a cream. Anything past that is color, and color is optional.</p>
  <p>The basket in the photograph is a reminder, not a dare: the pieces should be able to leave the house with you. If a bottle needs a manual, it is not in this edit.</p>
  <p>Start with <a href="product-foaming-cleanse.html">Everyday Foaming Cleanse</a> on damp skin. Follow with <a href="product-dew-serum.html">Hyaluronic Dew Serum</a> while the face is still wet. Seal it.</p>
</article>
<article class="essay wrap" id="glow-essay">
  <p class="eyebrow">Essay</p>
  <h2>Get your glow on.</h2>
  {img("glow.png", "The glow ritual", "50% 40%", 736, 736)}
  <p>Glow, here, is water and light, not glitter. The rose packaging is only the outside. Inside, the formulas are plain: a gentle foam, hyaluronic acid with a quiet vitamin C, and a cream that does not fight the foundation.</p>
  <p>Use them in order. Serum on dry skin pills. Cream before serum slides off. The ritual is the sequence.</p>
</article>
<article class="essay wrap" id="tools-essay">
  <p class="eyebrow">Essay</p>
  <h2>Care, in the hand.</h2>
  {img("tools.png", "Beauty care tools", "50% 55%")}
  <p>Foundation changes with the tool. Fingers leave it richer. The <a href="product-cloud-sponge.html">Cloud Sponge</a>, used damp, makes Luminous Veil look like skin. The <a href="product-powder-brush.html">powder brush</a> is for blush only after the complexion has settled.</p>
  <p>Wash the brush. Replace the sponge when the point goes soft. Tools are not decorations.</p>
</article>
"""
    return shell("Journal — Helalune", "journal", body, "Helalune journal: everyday glow, the skincare ritual, and care tools.")


def page_contact():
    body = f"""
<header class="page-head wrap">
  <p class="eyebrow">Contact</p>
  <h1>Write to the atelier.</h1>
</header>
<div class="split wrap">
  <div class="visit-card">
    <p class="eyebrow">Write</p>
    <p>Helalune</p>
    <p><a href="mailto:hello@helalune.com">hello@helalune.com</a></p>
    <p class="fine" style="margin-top:1rem">The note stays on this page. In this preview it is not emailed.</p>
  </div>
  <div id="sent">
    <form class="fields" action="#sent" method="get">
      <label class="field"><span>Name</span><input required autocomplete="name"></label>
      <label class="field"><span>Email</span><input type="email" required autocomplete="email"></label>
      <label class="field wide"><span>Note</span><textarea required placeholder="A shade question, an appointment, a piece you cannot find."></textarea></label>
      <div class="field wide"><button class="btn" type="submit">Send the note</button></div>
    </form>
    <p class="joined">The note is ready. The atelier would answer from hello@helalune.com.</p>
  </div>
</div>
<figure class="wrap" style="padding-bottom:4rem">{img("storefront.png", "The Helalune storefront edit", "50% 35%")}</figure>
"""
    return shell("Contact — Helalune", "about", body, "Write to Helalune.")


def page_account():
    body = """
<div class="account wrap">
  <input class="state" type="radio" name="acct" id="tab-in" checked>
  <input class="state" type="radio" name="acct" id="tab-up">
  <header class="page-head" style="padding-left:0;padding-right:0">
    <p class="eyebrow">Account</p>
    <h1>The salon.</h1>
    <p class="lede">Sign in to leave a name on this page. Passwords are not sent anywhere.</p>
  </header>
  <p class="joined" id="welcome">Welcome in. This sign-in lives only on the page, which is the honest limit of an HTML salon.</p>
  <div class="tabs">
    <label for="tab-in">Sign in</label>
    <label for="tab-up">Create account</label>
  </div>
  <form class="sheet in" action="#welcome" method="get">
    <label class="field"><span>Email</span><input type="email" required autocomplete="username"></label>
    <label class="field"><span>Password</span><input type="password" required minlength="8" autocomplete="current-password"></label>
    <button class="btn" type="submit">Sign in</button>
  </form>
  <form class="sheet up" action="#welcome" method="get">
    <label class="field"><span>Name</span><input required autocomplete="name"></label>
    <label class="field"><span>Email</span><input type="email" required autocomplete="email"></label>
    <label class="field"><span>Password</span><input type="password" required minlength="8" autocomplete="new-password"></label>
    <button class="btn" type="submit">Create account</button>
  </form>
</div>
"""
    return shell("Account — Helalune", "account", body, "Sign in to the Helalune salon.")


def page_plain(current, eyebrow, title, lede, blocks, description):
    parts = [f"<h2>{escape(h)}</h2><p>{p}</p>" for h, p in blocks]
    body = f"""
<header class="page-head wrap">
  <p class="eyebrow">{escape(eyebrow)}</p>
  <h1>{escape(title)}</h1>
  <p class="lede">{escape(lede)}</p>
</header>
<div class="prose wrap">{''.join(parts)}</div>
"""
    return shell(f"{title} — Helalune", current, body, description)


def page_faq():
    items = [
        ("How does the bag add up?", "Each piece is a square tick. The due amount on the right is rewritten for every combination, including the code HELALUNE10, which takes ten percent off the merchandise."),
        ("When is shipping free?", "From $120 of merchandise, before the code. Under that, delivery is $8."),
        ("How do I pay?", "Pay on delivery, or ask for a bank transfer after the order is confirmed. The site never asks for a card number."),
        ("Are the hoops real gold?", "No. The hoops are gold-tone and the cuff is champagne or silver-tone. Both are imitation jewelry, made to be worn with the nude edit."),
        ("Can I return a piece?", "Unworn, unused pieces within 14 days. Sponges and opened complexion, once the seal is broken, stay with you."),
        ("Where is fragrance?", "Not in this drop. The filter is there so the absence is clear. The letter will announce it."),
    ]
    details = "\n".join(
        f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in items
    )
    body = f"""
<header class="page-head wrap">
  <p class="eyebrow">Questions</p>
  <h1>Before you order.</h1>
</header>
<div class="prose wrap">{details}</div>
"""
    return shell("Questions — Helalune", "shop", body, "Shipping, payment, returns, and imitation jewelry at Helalune.")


def check_links(pages):
    missing = []
    for name, html in pages.items():
        for raw in html.split('href="')[1:]:
            href = raw.split('"', 1)[0]
            if href.startswith(("http", "mailto:", "#")):
                continue
            path = href.split("#", 1)[0]
            if not path:
                continue
            if not (ROOT / path).exists() and path not in pages:
                missing.append((name, href))
    return missing


def main():
    (ROOT / "css").mkdir(exist_ok=True)
    (ROOT / "css" / "totals.css").write_text(totals_css(), encoding="utf-8")
    pages = {
        "index.html": page_home(),
        "shop.html": page_shop(),
        "cart.html": page_bag("bag"),
        "checkout.html": page_bag("checkout"),
        "order.html": page_order(),
        "about.html": page_about(),
        "journal.html": page_journal(),
        "contact.html": page_contact(),
        "account.html": page_account(),
        "faq.html": page_faq(),
    }
    pages["shipping.html"] = page_plain(
        "shop",
        "Shipping",
        "Delivery.",
        "Orders of $120 or more ship complimentary. Below that, delivery is $8.",
        [
            ("Cost", "Complimentary from $120 of merchandise. Under that, delivery is $8."),
            ("Timing", "Saturday to Thursday. Orders placed before noon leave the same day when the route allows."),
            ("Payment on arrival", "Have the due amount ready. The confirmation page shows the number from your bag. We do not take card numbers on the site."),
        ],
        "Helalune shipping.",
    )
    pages["returns.html"] = page_plain(
        "shop",
        "Returns",
        "Fourteen quiet days.",
        "If a shade is wrong, send it back unused.",
        [
            ("What can return", "Unworn jewelry, unused brushes, and sealed skincare or makeup within 14 days of delivery."),
            ("What stays", "The sponge once it is damp, and any complexion or lip color once the seal is open."),
            ("How", "Write through the contact page with your order number HL-20481 and the piece name."),
        ],
        "Helalune returns within fourteen days.",
    )
    pages["privacy.html"] = page_plain(
        "about",
        "Privacy",
        "What this page keeps.",
        "Helalune in this preview does not run a server account.",
        [
            ("Forms", "Names, notes, and delivery lines stay in your browser. Placing an order opens a confirmation page and does not transmit a card number, because we never ask for one."),
            ("The list", "The email field on the home page confirms on screen. It is not added to a mailing house from this preview."),
            ("Photographs", "Campaign images belong to the Helalune edit assembled for this storefront."),
        ],
        "How the Helalune preview handles notes and orders.",
    )
    for product in PRODUCTS:
        pages[f"product-{product['slug']}.html"] = page_product(product)
    for name, html in pages.items():
        (ROOT / name).write_text(html, encoding="utf-8")
    missing = check_links(pages)
    if missing:
        raise SystemExit(f"Missing links: {missing[:12]}")
    chosen, merch, discount, ship, due = quote_totals((1 << 0) | (1 << 3) | (1 << 8), False)
    assert merch == 144 and due == 144 and ship == 0, (merch, due, ship)
    chosen, merch, discount, ship, due = quote_totals((1 << 0) | (1 << 3) | (1 << 8), True)
    assert discount == 14 and due == 130, (discount, due)
    print(f"Wrote {len(pages)} pages and css/totals.css")


if __name__ == "__main__":
    main()
