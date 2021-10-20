class EntityConfig():
    ''' ENTITY TYPE NAMES '''
    SILICON_TYPE = "SILICON"
    PROJECT_TYPE = "PROJECT"
    PBA_TYPE = "PBA"
    REWORK_TYPE = "REWORK"
    SUBMISSION_TYPE = "SUBMISSION"
    RUNID_TYPE = "RUNID"

    ''' SILICON CONFIG '''
    SILICON_FILTERS = ["name"]
    SILICON_FILES = []

    ''' PROJECT CONFIG '''
    PROJECT_FILTERS = ["name"]
    PROJECT_FILES = []

    ''' PBA CONFIG '''
    PBA_FILTERS = ["part_number", "project"]
    PBA_FILES = []

    ''' REWORK CONFIG'''
    REWORK_FILTERS = ["rework", "pba"]
    REWORK_FILES = []

    ''' SUBMISSION CONFIG'''
    SUBMISSION_FILTERS = ["submission", "rework", "pba"]
    SUBMISSION_FILES = []

    ''' RUNID CONFIG '''
    RUNID_FILTERS = ["runid"]
    RUNID_FILES = [
        "Comments.txt",  # CommentsFileEntity
        "dut.csv",  #
        "dut.txt",  #
        "logfile.txt",  #
        "lp.csv",  #
        "lp.txt",  #
        "power.csv",  # RunidPowerCSVFileEntity
        "power.json",  #
        "settings.xml",  #
        "status.json",  # StatusFileEntity
        "steps.xml",  #
        "System Info.json",  # SystemInfoFileEntity
        "testrun.json"]  # TestRunFileEntity
