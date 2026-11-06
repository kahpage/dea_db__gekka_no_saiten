# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    i = 1  # ==== gekka_no_saiten1 ====
    if i not in disabled_events:
        event_name = f"gekka_no_saiten{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_gekka01-hyoushi.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070411050504/http://gekka.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="月下の祭典 カタログ表紙絵 伊倉ナギサ 様 （がんバレル）",
            ),
            Medium(
                "01_gekka01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20070306085429/http://gekka.ket.jp/gekka01-list.htm",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="月下の祭典 チラシ・ポスター 神崎かるな 様 （ぐりーんぺっぱー）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1590924, 136.9298891),
                address="2 Chome-6-3 Fukiage, Chikusa Ward, Nagoya, Aichi 464-0856, Japan",
                description="名古屋中小企業福祉会館６階ホール（名古屋・大須）",
                sources=[
                    Source(
                        "https://web.archive.org/web/20070411050504/http://gekka.ket.jp/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWkq7ADwtY0_LzlU3mk0DFlmJeNo1bo9bpZ2vqyiopbdHLCB4zA_pSkSpa9YKGQsJgPRhkx6a0R8e8OPBlstCq-5saYTJ5-avtnX6fZR-cI6YHIZgV7pYeOLMsw_PDlSU2wW-9f9=s0?imgmax=0",
                url="https://maps.app.goo.gl/5QerDbUB3hz5Xcjq9",
            ),
        ]
        event = Event(
            aliases=[
                "月下の祭典",
                "Gekka no Saiten",
                "月下の祭典1",
                "Gekka no Saiten 1",
            ],
            dates="2006.11.12",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20070411050504/http://gekka.ket.jp/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20070306085429/http://gekka.ket.jp/gekka01-list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with まきますか？まきませんか？ex and リリカルハート",
            # comments=None,
            last_edited="2026.11.01",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== gekka_no_saiten2 ====
    if i not in disabled_events:
        event_name = f"gekka_no_saiten{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_gekka02.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20111123212926/http://gekka.ket.jp/",
                        (RT.Reliable, OT.Official),
                    )
                ],
                comments="月下の祭典２ チラシ絵 かつまたかずき 様 （THIRD BRAND）",
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.01365, 135.7809429),
                address="9-1 Okazaki Seishojicho, Sakyo Ward, Kyoto, 606-8343, Japan",
                description="京都市勧業館みやこめっせ 地下１階 第１展示場",
                sources=[
                    Source(
                        "https://web.archive.org/web/20111123212926/http://gekka.ket.jp/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlur6oWztq77DaOuTZLw5MRyj3iDVD1CD-wl9_7wkEXC7e9JYhls5YX8XY6_936CE_RWP6CozLolZI73Mh7gleO-PgU9DJro4VpNaq7nQSPaHd9rChZ-VVge7urD47mbsVOMZ6B-A=s870-k-no",
                url="https://maps.app.goo.gl/8MjxYFEFKBxjhyTT8",
            ),
        ]
        event = Event(
            aliases=["月下の祭典2", "Gekka no Saiten 2"],
            dates="2007.09.23",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20111123212926/http://gekka.ket.jp/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20071016204745/http://gekka.ket.jp/gekka02-list.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.11.01",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "returns"  # ==== gekka_no_saitenreturns ====
    if i not in disabled_events:
        event_name = f"gekka_no_saiten{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            Medium(
                "returns_banner.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20180722134217/http://ttc.ninja-web.net/gekka/banner.jpg",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.1313699, 136.8980176),
                address="1-1 Atsuta Nishimachi, Atsuta Ward, Nagoya, Aichi 456-0036, Japan",
                description="名古屋国際会議場 白鳥ホール （名古屋市熱田区）",
                sources=[
                    Source(
                        "https://web.archive.org/web/20190311201958/http://ttc.ninja-web.net/gekka/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn7Lqm9_Q0NEdha1ASXnQ5vdfjHbPJAbiquEME-dTc0IQlVMwwldl4PgCGmoqwXy7f1H0VzeeQ34Sfh31dwy-yLo6SG1i6J7RxOt2LCAXGM3sea6CVPSdGtLv8BqQvcjQ9wGbdq8g=s0?imgmax=0",
                url="https://maps.app.goo.gl/WvWpsu1s7P6fTsdj9",
            ),
        ]
        event = Event(
            aliases=["月下の祭典Returns", "Gekka no Saiten Returns"],
            dates="2018.11.04",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20190311201958/http://ttc.ninja-web.net/gekka/",
                    (RT.Reliable, OT.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
            ],
            locations=locations,
            description="Part of the 名古屋熱田同人祭2018秋 joint venue, featuring ツインテールカーニバル9, 制服宣言2, 絶対ニーソ, 百合乙女の楽園, 艦隊ぱれーど２, 御城まつり, 月下の祭典Returns, アズールフェスタ, BanG Dreamer's Party! in 名古屋 and 魔法少女本作製計画SP",
            # comments=None,
            last_edited="2026.11.01",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== gekka_no_saiten ====
    # if i not in disabled_events:
    #     event_name = f"gekka_no_saiten{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=["月下の祭典", "Gekka no Saiten "],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.11.01",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        Medium(
            "eg_gekka-bn00.jpg",
            [
                Source(
                    "https://web.archive.org/web/20060616181444/http://gekka.ket.jp/",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        Medium(
            "eg_gekka-bn01.jpg",
            [
                Source(
                    "https://web.archive.org/web/20060616181444/http://gekka.ket.jp/",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        Medium(
            "eg_gekka-bn02.jpg",
            [
                Source(
                    "https://web.archive.org/web/20100412153547/http://gekka.ket.jp/",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        Medium(
            "eg_gekka-bn03.jpg",
            [
                Source(
                    "https://web.archive.org/web/20100412153547/http://gekka.ket.jp/",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        Medium(
            "eg_gekka-bn.jpg",
            [
                Source(
                    "https://web.archive.org/web/20100412153547/http://gekka.ket.jp/",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = ["http://gekka.ket.jp/", "http://ttc.ninja-web.net/gekka/"]

    event_group = EventGroup(
        aliases=[
            "月下の祭典",
            "Gekka no Saiten",
        ],
        events=events,
        media=media,
        links=links,
        sources=[
            # Source(
            #     "",
            #     (ReliabilityTypes.Reliable, OriginTypes.Official),
            # ),
        ],
        comments=None,
        description=None,
        last_edited="2026.11.01",
    )

    # Check for missing media files and unreferenced media files
    media = [m for e in event_group.events for m in e.media or []] + (event_group.media or [])
    for m in media:
        if m.path.startswith(("http://", "https://")):
            continue
        p = PATH_MEDIA / m.path
        if not p.exists():
            print(f"Warning: Medium file not found: {p}")

    referenced = {m.path for m in media}
    for p in PATH_MEDIA.rglob("*"):
        if p.is_file() and p.relative_to(PATH_MEDIA).as_posix() not in referenced:
            print(f"Warning: Media file not referenced in event group: {p}")

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
