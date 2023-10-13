from katwarn_api import KatWarnApi
from katwarn_api.utils import Service


def test_topics(requests_mock):
    requests_mock.get(
        Service.create("content").url + "/topics",
        text='{"topics": ["5d921d811c401fb083ef105d", "5d80c5c63552aff16f164b84"]}',
    )
    topics = KatWarnApi().get_topics()
    assert topics.topics == ["5d921d811c401fb083ef105d", "5d80c5c63552aff16f164b84"]
