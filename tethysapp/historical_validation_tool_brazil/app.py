from tethys_sdk.base import TethysAppBase


class HistoricalValidationToolBrazil(TethysAppBase):
    """
    Tethys app class for Historical Validation Tool Brazil.
    """

    name = 'Historical Validation Tool Brazil'
    description = ''
    package = 'historical_validation_tool_brazil'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'historical-validation-tool-brazil'
    color = '#009c3b'
    tags = ''
    enable_feedback = False
    feedback_emails = []