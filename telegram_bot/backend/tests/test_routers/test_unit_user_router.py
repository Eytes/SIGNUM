import responses
import pytest
from tests.conftest import (
    client,
    not_found_nickname,
    full_statistic_data,
    min_statistic_data
)
from codewars.user_statistic import CODEWARS_GET_USER_URL


@pytest.mark.parametrize(
    "show_full_statistic, nickname, expected_status, expected_statistic",
    [
        (True, "Eytes", 200, full_statistic_data),
        (False, "Eytes", 200, min_statistic_data),
        (True, "hlvskdjvlskjdfvksjd", 404, not_found_nickname),
        (False, "hlvskdjvlskjdfvksjd", 404, not_found_nickname),
        (True, -1231, 404, not_found_nickname),
        (True, "312-312", 404, not_found_nickname),
        (True, ".!", 404, not_found_nickname),
    ]
)
@responses.activate
def test_get_statistic_by_nickname(show_full_statistic, nickname, expected_status, expected_statistic):
    responses.add(
        responses.GET,
        CODEWARS_GET_USER_URL.format(nickname=nickname),
        json=expected_statistic,
        status=expected_status,
    )
    response = client.get(f'/user/statistic_by_codewars_nickname/{show_full_statistic}/{nickname}')
    assert response.status_code == expected_status
    assert response.json() == expected_statistic
