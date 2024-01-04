import pytest
import responses

from config import settings
from tests.conftest import (
    client,
    not_found_nickname,
    full_statistic_data,
    min_statistic_data,
)


@pytest.mark.parametrize(
    "show_full_statistic, nickname, expected_status, expected_statistic",
    [
        (True, "Eytes", 200, full_statistic_data),
        (False, "Eytes", 200, min_statistic_data),
        (True, "hlvskdjvlskjdfvksjd", 404, not_found_nickname),
        (False, "hlvskdjvlskjdfvksjd", 404, not_found_nickname),
        (True, "-1231", 404, not_found_nickname),
        (True, "312-312", 404, not_found_nickname),
        (True, ".!", 404, not_found_nickname),
    ],
)
@responses.activate
def test_get_statistic_by_nickname(
    show_full_statistic, nickname, expected_status, expected_statistic
):
    responses.add(
        responses.GET,
        settings.codewars_get_user_url + nickname,
        json=expected_statistic,
        status=expected_status,
    )
    response = client.get(
        settings.prefix_api_v1
        + settings.prefix_user_router
        + f"/statistic_by_codewars_nickname/{show_full_statistic}/{nickname}"
    )
    assert response.status_code == expected_status
    assert response.json() == expected_statistic
