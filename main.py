from argparse import ArgumentParser
VersionID = """1	1.6.1（13w24a）到1.8.9\n
2	1.9（15w31a）到1.10.2\n
3	1.11（16w32a）到1.12.2（17w47b）\n
4	1.13（17w48a）到1.14.4（19w46b）\n
5	1.15（1.15-pre1）到1.16.1（1.16.2-pre3）\n
6	1.16.2（1.16.2-rc1）到1.16.5\n
7	1.17（20w45a）到1.17.1（21w38a）\n
8	1.18（21w39a）到1.18.2\n
9	1.19（22w11a）到1.19.2\n
11	1.19.3快照22w42a到22w44a\n
12	1.19.3（22w45a）到1.19.4快照23w07a\n
13	1.19.4（1.19.4-pre1）到1.20快照23w13a\n
14	1.20快照23w14a到23w16a\n
15	1.20（23w17a）到1.20.1\n
16	1.20.2快照23w31a\n
17	1.20.2快照23w32a到1.20.2-pre1\n
18	1.20.2（1.20.2-pre2）到1.20.3快照23w41a\n
19	1.20.3快照23w42a\n
20	1.20.3快照23w43a到23w44a\n
21	1.20.3快照23w45a到23w46a\n
22	1.20.3（1.20.3-pre1）到1.20.4（23w51b）\n
24	1.20.5快照24w03a到24w04a\n
25	1.20.5快照24w05a到24w05b\n
26	1.20.5快照24w06a到24w07a\n
28	1.20.5快照24w09a到24w10a\n
29	1.20.5快照24w11a\n
30	1.20.5快照24w12a\n
31	1.20.5快照24w13a到1.20.5-pre3\n
32	1.20.5（1.20.5-pre4）到1.20.6\n
33	1.21快照24w18a到24w20a\n
34	1.21快照24w21a及以上\n
"""
argparser = ArgumentParser()
argparser.add_argument("-m", "--mod", help="The path of the mod jar file or the resource pack zip file", required=True)
argparser.add_argument("-n", "--namespace", help="The namespace of the mod", required=True)
argparser.add_argument("-s", "--source", help="The source language of the mod", required=True)
argparser.add_argument("-t", "--target", help="The target language of the mod", required=True)
argparser.add_argument("-v", "--version", help=f"""The version id of Minecraft which can run this mod(Not like: 1.XX)\nMore:https://minecraft.wiki/w/Resource_pack""", required=False, default="4")
argparser.add_argument("-no-gui", help="Disable the GUI", action="store_true")

argparser.parse_args()