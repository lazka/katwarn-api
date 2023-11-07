# SPDX-License-Identifier: MIT

import datetime
from enum import Enum
from typing import NamedTuple, Optional

from pydantic import BaseModel


class ContentType(str, Enum):
    clear = "clear"
    info = "info"
    warning = "warning"


class Severity(str, Enum):
    minor = "minor"
    moderate = "moderate"
    severe = "severe"
    extreme = "extreme"


class EventCode(str, Enum):
    _911Service = "911Service"
    """911 Service"""

    accident = "accident"
    """Motor Vehicle Accident"""

    admin = "admin"
    """Administration"""

    airQuality = "airQuality"
    """Air Quality"""

    aircraft = "aircraft"
    """Aircraft Incident"""

    aircraftCras = "aircraftCras"
    """Aircraft Crash"""

    airportClose = "airportClose"
    """Airport Closure"""

    airspaceClos = "airspaceClos"
    """Airspace Closure"""

    amber = "amber"
    """Missing Child (AMBER)"""

    ambulance = "ambulance"
    """Ambulance"""

    animalDang = "animalDang"
    """Dangerous Animal"""

    animalDiseas = "animalDiseas"
    """Animal Disease"""

    animalFeed = "animalFeed"
    """Animal Feed"""

    animalHealth = "animalHealth"
    """Animal Health"""

    arcticOut = "arcticOut"
    """Arctic Outflow"""

    avalanche = "avalanche"
    """Avalanche"""

    aviation = "aviation"
    """Aviation"""

    biological = "biological"
    """Biological Hazard"""

    blizzard = "blizzard"
    """Blizzard"""

    bloodSupply = "bloodSupply"
    """Blood Supply"""

    blowingSnow = "blowingSnow"
    """Blowing Snow"""

    bridgeClose = "bridgeClose"
    """Bridge Closure"""

    cable = "cable"
    """Cable Service"""

    chemical = "chemical"
    """Chemical Hazard"""

    civil = "civil"
    """Information"""

    civilEmerg = "civilEmerg"
    """Civil Emergency"""

    civilEvent = "civilEvent"
    """Public Event"""

    cold = "cold"
    """Extreme Cold"""

    coldWave = "coldWave"
    """Cold Wave"""

    crime = "crime"
    """Police Operation"""

    cyberCrime = "cyberCrime"
    """Cyber Crime"""

    damBreach = "damBreach"
    """Dam Breach"""

    damOverflow = "damOverflow"
    """Dam Overflow"""

    dangerPerson = "dangerPerson"
    """Dangerous Person"""

    demonstration = "demonstration"
    """Demonstration"""

    diesel = "diesel"
    """Diesel Supply"""

    drinkingWate = "drinkingWate"
    """Drinking Water"""

    drugSafety = "drugSafety"
    """Drug Safety"""

    drugSupply = "drugSupply"
    """Drug Supply"""

    dustStorm = "dustStorm"
    """Dust Storm"""

    earthquake = "earthquake"
    """Earthquake"""

    electric = "electric"
    """Electricity Supply"""

    emergFacil = "emergFacil"
    """Emergency Support Facilities"""

    emergSupport = "emergSupport"
    """Emergency Support Services"""

    evacuation = "evacuation"
    """Evacuation"""

    explosive = "explosive"
    """Explosive Hazard"""

    facility = "facility"
    """Service or Facility"""

    fallObject = "fallObject"
    """Falling Objects"""

    fire = "fire"
    """Major Fire"""

    flashFlood = "flashFlood"
    """Flash Flood"""

    flashFreeze = "flashFreeze"
    """Flash Freeze"""

    flood = "flood"
    """Flood"""

    fog = "fog"
    """Fog"""

    foodSafety = "foodSafety"
    """Food Safety"""

    foodSupply = "foodSupply"
    """Food Supply"""

    forestFire = "forestFire"
    """Forest Fire"""

    freezeDrzl = "freezeDrzl"
    """Freezing Rain"""

    freezeRain = "freezeRain"
    """Freezing Rain"""

    freezngSpray = "freezngSpray"
    """Freezing Spray"""

    frost = "frost"
    """Extreme Frost"""

    galeWind = "galeWind"
    """Gale Wind"""

    gasoline = "gasoline"
    """Gasoline Supply"""

    geophysical = "geophysical"
    """Geophysical"""

    hazmat = "hazmat"
    """Hazardous Materials"""

    health = "health"
    """Health"""

    heat = "heat"
    """High Heat"""

    heatHumidity = "heatHumidity"
    """High Humidity"""

    heatWave = "heatWave"
    """Heat Wave"""

    heatingOil = "heatingOil"
    """Heating Oil Supply"""

    highWater = "highWater"
    """High Water Level"""

    homeCrime = "homeCrime"
    """Police Operation"""

    hospital = "hospital"
    """Hospital"""

    hurricFrcWnd = "hurricFrcWnd"
    """Hurricane Force Wind"""

    hurricane = "hurricane"
    """Hurricane"""

    ice = "ice"
    """Ice"""

    icePressure = "icePressure"
    """Ice Pressure"""

    iceberg = "iceberg"
    """Iceberg"""

    industCrime = "industCrime"
    """Police Operation"""

    industryFire = "industryFire"
    """Major Fire"""

    infectious = "infectious"
    """Infectious Disease"""

    internet = "internet"
    """Internet Service"""

    lahar = "lahar"
    """Lahar"""

    landslide = "landslide"
    """Landslide"""

    lavaFlow = "lavaFlow"
    """Lava Flow"""

    magnetStorm = "magnetStorm"
    """Magnetic Storm"""

    marine = "marine"
    """Marine"""

    marineSecure = "marineSecure"
    """Marine Security"""

    meteor = "meteor"
    """Meteorite"""

    missingPer = "missingPer"
    """Missing Person"""

    missingVPer = "missingVPer"
    """Missing Person"""

    naturalGas = "naturalGas"
    """Natural Gas Supply"""

    nautical = "nautical"
    """Nautical Incident"""

    notam = "notam"
    """Notice to Airmen"""

    other = "other"
    """Special Message"""

    overflood = "overflood"
    """Overland Flow Flood"""

    plant = "plant"
    """Plant Health"""

    plantInfect = "plantInfect"
    """Plant Infectious Disease"""

    product = "product"
    """Product Safety"""

    publicServic = "publicServic"
    """Public Services"""

    pyroclaSurge = "pyroclaSurge"
    """Pyroclastic Surge"""

    pyroclasFlow = "pyroclasFlow"
    """Pyroclastic Flow"""

    radiological = "radiological"
    """Radiological Hazard"""

    railway = "railway"
    """Railway"""

    rainfall = "rainfall"
    """Rainfall"""

    rdCondition = "rdCondition"
    """Hazardous Road Conditions"""

    reminder = "reminder"
    """Reminder"""

    rescue = "rescue"
    """Rescue"""

    retailCrime = "retailCrime"
    """Police Operation"""

    road = "road"
    """Road Traffic"""

    roadClose = "roadClose"
    """Roadway Closure"""

    roadDelay = "roadDelay"
    """Roadway Delay"""

    roadUsage = "roadUsage"
    """Roadway Usage Condition"""

    rpdCloseLead = "rpdCloseLead"
    """Rapid Closing of Coastal Leads"""

    satellite = "satellite"
    """Satellite Service"""

    schoolBus = "schoolBus"
    """School Bus"""

    schoolClose = "schoolClose"
    """School Closure"""

    schoolLock = "schoolLock"
    """School Lockdown"""

    sewer = "sewer"
    """Sewer System"""

    silver = "silver"
    """Missing Person"""

    snowSquall = "snowSquall"
    """Snow Squall"""

    snowfall = "snowfall"
    """Snowfall"""

    spclIce = "spclIce"
    """Special Ice"""

    spclMarine = "spclMarine"
    """Special Marine"""

    squall = "squall"
    """Squall"""

    storm = "storm"
    """Extreme Weather"""

    stormFrcWnd = "stormFrcWnd"
    """Storm Force Wind"""

    stormSurge = "stormSurge"
    """Storm Surge"""

    strike = "strike"
    """Strike"""

    strongWind = "strongWind"
    """Strong Wind"""

    telephone = "telephone"
    """Telephone Service"""

    temperature = "temperature"
    """Extreme Temperatures"""

    terrorism = "terrorism"
    """Terrorism"""

    testMessage = "testMessage"
    """Test Message"""

    thunderstorm = "thunderstorm"
    """Thunderstorm"""

    tornado = "tornado"
    """Tornado"""

    traffic = "traffic"
    """Traffic Report"""

    train = "train"
    """Train Accident"""

    transit = "transit"
    """Public Transit"""

    tropStorm = "tropStorm"
    """Tropical Storm"""

    tsunami = "tsunami"
    """Tsunami"""

    urbanFire = "urbanFire"
    """Major Fire"""

    utility = "utility"
    """Utility"""

    vehicleCrime = "vehicleCrime"
    """Police Operation"""

    volcanicAsh = "volcanicAsh"
    """Volcano Ash Cloud"""

    volcano = "volcano"
    """Volcano"""

    volunteer = "volunteer"
    """Volunteer Request"""

    warfareMater = "warfareMater"
    """Warfare Material"""

    waste = "waste"
    """Waste Management"""

    water = "water"
    """Water Supply"""

    waterPollut = "waterPollut"
    """Water Pollution"""

    waterQuality = "waterQuality"
    """Water Quality"""

    waterspout = "waterspout"
    """Waterspout"""

    weather = "weather"
    """Weather"""

    wildFire = "wildFire"
    """Wild Fire"""

    wind = "wind"
    """Wind"""

    windchill = "windchill"
    """Wind Chill"""

    winterStorm = "winterStorm"
    """Winter Storm"""


class BoundingBox(NamedTuple):
    xmin: float
    ymin: float
    xmax: float
    ymax: float


class ServiceAreasEntry(BaseModel, extra="forbid"):
    bbox: BoundingBox
    etag: str
    provider_id: str


class ServiceAreas(BaseModel, extra="forbid"):
    index: list[ServiceAreasEntry]


class ServiceAreaProperties(BaseModel, extra="forbid"):
    content_url: str
    longhand: str
    shorthand: str
    area_infos_available: Optional[bool] = False


class ServiceAreaObjectProperties(BaseModel, extra="forbid"):
    longhand: str
    shorthand: str
    priority: Optional[int] = None


class ServiceAreaInfosEntry(BaseModel, extra="forbid"):
    id: str
    etag: str


class ServiceAreaInfos(BaseModel, extra="forbid"):
    infos: list[ServiceAreaInfosEntry]


class ServiceAreaInfo(BaseModel, extra="forbid"):
    id: str


class ServiceArea(BaseModel, extra="forbid"):
    service_area: dict
    """TopoJSON"""


class IncidentsEntry(BaseModel, extra="forbid"):
    bbox: BoundingBox
    etag: str
    provider_id: str
    id: str


class Incident(BaseModel, extra="forbid"):
    alerts: list[str]
    bbox: BoundingBox
    id: str


class Incidents(BaseModel, extra="forbid"):
    incidents: list[IncidentsEntry]


class PreventionsEntry(BaseModel, extra="forbid"):
    id: str


class Preventions(BaseModel, extra="forbid"):
    messages: list[PreventionsEntry]


class Prevention(BaseModel, extra="forbid"):
    id: str
    language: str
    web: str
    subject: str
    description: str
    headline: str
    icon: dict[str, str]
    background: dict[str, str]


class AlertResource(BaseModel, extra="forbid"):
    mime_type: str
    uri: str


class AlertRestriction(BaseModel, extra="forbid"):
    topics: Optional[list[str]] = None
    spatial: Optional[str] = None


class BaseAlert(BaseModel, extra="forbid"):
    acknowledgeable: bool
    checksum: str
    content_type: ContentType
    description: Optional[str] = None
    effective: datetime.datetime
    event_code: EventCode
    expires: Optional[datetime.datetime] = None
    event_type: Optional[str] = None
    headline: str
    id: str
    issuer: str
    language: str
    locality: Optional[str] = None
    notifiable: bool
    provider_id: str
    resources: Optional[list[AlertResource]] = None
    restriction: Optional[AlertRestriction] = None
    sender_id: str
    sent: str
    severity: Severity
    subject: str
    web: Optional[str] = None
    instruction: Optional[list[str]] = None
    contact: Optional[str] = None
    references: Optional[str] = None
    visibility: Optional[str] = None


class TopicAlert(BaseAlert, extra="forbid"):
    pass


class Alert(BaseAlert, extra="forbid"):
    geometry: dict
    """GeoJSON"""


class Topics(BaseModel, extra="forbid"):
    topics: list[str]


class TopicIncident(BaseModel, extra="forbid"):
    id: str
    alerts: list[str]


class Topic(BaseModel, extra="forbid"):
    incidents: list[TopicIncident]


class TopicDescription(BaseModel, extra="forbid"):
    background: dict[str, str]
    category: str
    description: str
    etag: str
    icon: dict[str, str]
    id: str
    label: str
    language: str
    provider_id: str
    recommended: bool
    sharable: bool
    sublabel: str
    web: Optional[str] = None
