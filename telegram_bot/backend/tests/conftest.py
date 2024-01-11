from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

not_found_nickname = {"detail": "Not Found"}

full_statistic_data = {
    "id": "123213321asdasdasdasd",
    "username": "Eytes",
    "name": None,
    "honor": 281,
    "clan": None,
    "leaderboardPosition": 259821,
    "skills": None,
    "ranks": {
        "overall": {
            "rank": -5,
            "name": "5 kyu",
            "color": "yellow",
            "score": 288,
        },
        "languages": {
            "python": {
                "rank": -6,
                "name": "6 kyu",
                "color": "yellow",
                "score": 221,
            },
            "cpp": {
                "rank": -8,
                "name": "8 kyu",
                "color": "white",
                "score": 19,
            },
            "javascript": {
                "rank": -7,
                "name": "7 kyu",
                "color": "white",
                "score": 46,
            },
            "java": {
                "rank": -8,
                "name": "8 kyu",
                "color": "white",
                "score": 16,
            },
        },
    },
    "codeChallenges": {
        "totalAuthored": 0,
        "totalCompleted": 57,
    },
}

min_statistic_data = {
    "honor": 281,
    "skills": None,
    "ranks": {
        "overall": {
            "rank": -5,
            "name": "5 kyu",
            "color": "yellow",
            "score": 288,
        },
        "languages": {
            "python": {
                "rank": -6,
                "name": "6 kyu",
                "color": "yellow",
                "score": 221,
            },
            "cpp": {
                "rank": -8,
                "name": "8 kyu",
                "color": "white",
                "score": 19,
            },
            "javascript": {
                "rank": -7,
                "name": "7 kyu",
                "color": "white",
                "score": 46,
            },
            "java": {
                "rank": -8,
                "name": "8 kyu",
                "color": "white",
                "score": 16,
            },
        },
    },
    "codeChallenges": {
        "totalAuthored": 0,
        "totalCompleted": 57,
    },
}

# TODO: прописывать фикстуры ниже
