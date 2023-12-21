import pytest
from tests.conftest import client


@pytest.mark.parametrize(
    'show_full_statistic, telegram_id, expected_status, expected_value',
    [
        (True, 123, 404, {'detail': 'Not Found'}),
        (True, 1, 404, {'detail': 'Not Found'}),
        (True, 132541235132, 404, {'detail': 'Not Found'}),
        (True, -1237645, 404, {'detail': 'Not Found'}),
    ]
)
def test_get_statistic(show_full_statistic, telegram_id, expected_status, expected_value):
    # TODO: сделать тестирование через МОК
    response = client.get(f'/user/{show_full_statistic}/{telegram_id}', timeout=5)
    assert response.status_code == expected_status
    assert response.json() == expected_value
