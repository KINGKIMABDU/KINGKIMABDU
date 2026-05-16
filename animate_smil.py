import os

repo_dir = r"C:\CODING\KINGKIMABDU\cards"

def get_slide_up(begin, translateY=15):
    return f'''<g opacity="0" transform="translate(0, {translateY})">
<animate attributeName="opacity" from="0" to="1" dur="0.8s" begin="{begin}s" fill="freeze" calcMode="spline" keySplines="0.05 0.7 0.1 1" keyTimes="0;1"/>
<animateTransform attributeName="transform" type="translate" from="0 {translateY}" to="0 0" dur="0.8s" begin="{begin}s" fill="freeze" calcMode="spline" keySplines="0.05 0.7 0.1 1" keyTimes="0;1"/>\n'''

def get_slide_right(begin, translateX=-15):
    return f'''<g opacity="0" transform="translate({translateX}, 0)">
<animate attributeName="opacity" from="0" to="1" dur="0.8s" begin="{begin}s" fill="freeze" calcMode="spline" keySplines="0.05 0.7 0.1 1" keyTimes="0;1"/>
<animateTransform attributeName="transform" type="translate" from="{translateX} 0" to="0 0" dur="0.8s" begin="{begin}s" fill="freeze" calcMode="spline" keySplines="0.05 0.7 0.1 1" keyTimes="0;1"/>\n'''

# -----------------
# 1. header.svg
# -----------------
header_path = os.path.join(repo_dir, "header.svg")
with open(header_path, "r", encoding="utf-8") as f:
    header = f.read()

header = header.replace("<!-- Avatar circle -->", f"<!-- Avatar circle -->\n{get_slide_up(0.1)}")
header = header.replace('preserveAspectRatio="xMidYMid slice" />', 'preserveAspectRatio="xMidYMid slice" />\n</g>')

header = header.replace("<!-- Name -->", f"{get_slide_up(0.2)}\n<!-- Name -->")
header = header.replace("킹키마브두</text>", "킹키마브두</text>\n</g>")

header = header.replace("<!-- Chips row -->", f"{get_slide_up(0.3)}\n<!-- Chips row -->")
header = header.replace("Developer</text>", "Developer</text>\n</g>")

with open(header_path, "w", encoding="utf-8") as f:
    f.write(header)

# -----------------
# 2. about.svg
# -----------------
about_path = os.path.join(repo_dir, "about.svg")
with open(about_path, "r", encoding="utf-8") as f:
    about = f.read()

about = about.replace('<text x="40" y="78"', f'{get_slide_up(0.1)}<text x="40" y="78"')
about = about.replace('Abdullah_Alhariri:</tspan></text>', 'Abdullah_Alhariri:</tspan></text>\n</g>')

about = about.replace('<text x="40" y="114"', f'{get_slide_up(0.2)}<text x="40" y="114"')
about = about.replace('Germany 🇩🇪"</tspan></text>', 'Germany 🇩🇪"</tspan></text>\n</g>')

about = about.replace('<text x="40" y="168"', f'{get_slide_up(0.3)}<text x="40" y="168"')
about = about.replace('366" font-family="\'Courier New\',Courier,monospace" font-size="13"><tspan class="t1">    ]</tspan></text>', '366" font-family="\'Courier New\',Courier,monospace" font-size="13"><tspan class="t1">    ]</tspan></text>\n</g>')

about = about.replace('<text x="40" y="402"', f'{get_slide_up(0.4)}<text x="40" y="402"')
about = about.replace('474" font-family="\'Courier New\',Courier,monospace" font-size="13"><tspan class="t1">    }</tspan></text>', '474" font-family="\'Courier New\',Courier,monospace" font-size="13"><tspan class="t1">    }</tspan></text>\n</g>')

about = about.replace('<text x="40" y="510"', f'{get_slide_up(0.5)}<text x="40" y="510"')
about = about.replace('636" font-family="\'Courier New\',Courier,monospace" font-size="13"><tspan class="t1">        ]</tspan></text>', '636" font-family="\'Courier New\',Courier,monospace" font-size="13"><tspan class="t1">        ]</tspan></text>\n</g>')

with open(about_path, "w", encoding="utf-8") as f:
    f.write(about)

# -----------------
# 3. stack.svg
# -----------------
stack_path = os.path.join(repo_dir, "stack.svg")
with open(stack_path, "r", encoding="utf-8") as f:
    stack = f.read()

stack = stack.replace('<rect class="cf"  x="32"', f'{get_slide_up(0.1)}<rect class="cf"  x="32"')
stack = stack.replace('middle">Python</text>', 'middle">Python</text>\n</g>')

stack = stack.replace('<rect class="cf"  x="116"', f'{get_slide_up(0.2)}<rect class="cf"  x="116"')
stack = stack.replace('middle">Java</text>', 'middle">Java</text>\n</g>')

stack = stack.replace('<rect class="cf"  x="184"', f'{get_slide_up(0.3)}<rect class="cf"  x="184"')
stack = stack.replace('middle">HTML · CSS</text>', 'middle">HTML · CSS</text>\n</g>')

stack = stack.replace('<rect class="cf"  x="292"', f'{get_slide_up(0.4)}<rect class="cf"  x="292"')
stack = stack.replace('middle">Firebase</text>', 'middle">Firebase</text>\n</g>')

stack = stack.replace('<rect class="cf"  x="384"', f'{get_slide_up(0.5)}<rect class="cf"  x="384"')
stack = stack.replace('middle">Git</text>', 'middle">Git</text>\n</g>')

stack = stack.replace('<rect class="cob" x="32"', f'{get_slide_up(0.6)}<rect class="cob" x="32"')
stack = stack.replace('middle">VS Code</text>', 'middle">VS Code</text>\n</g>')

with open(stack_path, "w", encoding="utf-8") as f:
    f.write(stack)

# -----------------
# 4. setup.svg
# -----------------
setup_path = os.path.join(repo_dir, "setup.svg")
with open(setup_path, "r", encoding="utf-8") as f:
    setup = f.read()

setup = setup.replace('<!-- Item 1 -->', f'<!-- Item 1 -->\n{get_slide_right(0.1)}')
setup = setup.replace('Primary phone</text>', 'Primary phone</text>\n</g>')

setup = setup.replace('<!-- Item 2 -->', f'<!-- Item 2 -->\n{get_slide_right(0.2)}')
setup = setup.replace('Main workstation &amp; Gaming</text>', 'Main workstation &amp; Gaming</text>\n</g>')

setup = setup.replace('<!-- Item 3 -->', f'<!-- Item 3 -->\n{get_slide_right(0.3)}')
setup = setup.replace('Outdoor work</text>', 'Outdoor work</text>\n</g>')

setup = setup.replace('<!-- Item 4 -->', f'<!-- Item 4 -->\n{get_slide_right(0.4)}')
setup = setup.replace('Smartwatch, Health &amp; Fitness</text>', 'Smartwatch, Health &amp; Fitness</text>\n</g>')

setup = setup.replace('<!-- Item 5 -->', f'<!-- Item 5 -->\n{get_slide_right(0.5)}')
setup = setup.replace('For school</text>', 'For school</text>\n</g>')

with open(setup_path, "w", encoding="utf-8") as f:
    f.write(setup)

print("SMIL Animations added successfully!")
