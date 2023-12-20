import pytest
from tests.routers.fastapi_test_client import client


@pytest.mark.parametrize(
    'telegram_id, expected_status, expected_value',
    [
        (123, 404, None),
        (1, 404, None),
        (132541235132, 404, None),
        (-1237645, 404, None),

    ]
)
def test_get_statistic(telegram_id, expected_status, expected_value):
    # TODO: сделать тестирование через МОК
    response = client.get(f'/user/full_statistic/{telegram_id}', timeout=5)
    assert response.status_code == expected_status
    assert response.json() == expected_value
