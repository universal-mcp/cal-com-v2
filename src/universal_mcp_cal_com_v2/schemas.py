from typing import Any, Optional, List
from pydantic import BaseModel, Field

# Generated Response Models


class Getproviderdetailsresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Getprovideraccesstokenresponse(BaseModel):
    status: str


class GcalcontrollerRedirectresponse(BaseModel):
    status: str
    data: dict[str, Any]


class GcalcontrollerSaveresponse(BaseModel):
    url: str


class ListclientusersresponseDataItem(BaseModel):
    id: float
    email: str
    username: str
    name: str
    timeZone: str
    weekStart: str
    createdDate: str
    timeFormat: float
    defaultScheduleId: float
    locale: Optional[str] = None
    avatarUrl: Optional[str] = None


class Listclientusersresponse(BaseModel):
    status: str
    data: List[ListclientusersresponseDataItem]


class Createoauthclientuserresponse(BaseModel):
    status: str
    data: dict[str, Any]
    error: Optional[dict[str, Any]] = None


class Getoauthclientuserbyidresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Forcerefreshuserresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Createoauthclientwebhookresponse(BaseModel):
    status: str
    data: dict[str, Any]


class ListwebhooksbyclientidresponseDataItem(BaseModel):
    payloadTemplate: str
    oAuthClientId: str
    id: float
    triggers: List[dict[str, Any]]
    subscriberUrl: str
    active: bool
    secret: Optional[str] = None


class Listwebhooksbyclientidresponse(BaseModel):
    status: str
    data: List[ListwebhooksbyclientidresponseDataItem]


class Deleteclientwebhookresponse(BaseModel):
    status: str
    data: str


class ListorgattributesresponseDataItem(BaseModel):
    id: str
    teamId: float
    type: str
    name: str
    slug: str
    enabled: bool
    usersCanEditRelation: Optional[bool] = None


class Listorgattributesresponse(BaseModel):
    status: str
    data: List[ListorgattributesresponseDataItem]


class Createorgattributesresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Fetchorganizationattributebyidresponse(BaseModel):
    status: str
    data: Any


class Createorgattributeoptionresponse(BaseModel):
    status: str
    data: dict[str, Any]


class GetorgattributeoptionsresponseDataItem(BaseModel):
    id: str
    attributeId: str
    value: str
    slug: str


class Getorgattributeoptionsresponse(BaseModel):
    status: str
    data: List[GetorgattributeoptionsresponseDataItem]


class Setuserattributeoptionresponse(BaseModel):
    status: str
    data: dict[str, Any]


class GetuserorgattributeoptionsresponseDataItem(BaseModel):
    id: str
    attributeId: str
    value: str
    slug: str


class Getuserorgattributeoptionsresponse(BaseModel):
    status: str
    data: List[GetuserorgattributeoptionsresponseDataItem]


class Createeventtyperesponse(BaseModel):
    status: str
    data: Any


class ListeventtypesbyteamandorgresponseDataItemHostsItem(BaseModel):
    userId: float
    mandatory: Optional[bool] = None
    priority: Optional[str] = None
    name: str
    avatarUrl: Optional[str] = None


class ListeventtypesbyteamandorgresponseDataItem(BaseModel):
    id: float
    lengthInMinutes: float
    lengthInMinutesOptions: Optional[List[float]] = None
    title: str
    slug: str
    description: str
    locations: List[Any]
    bookingFields: List[Any]
    disableGuests: bool
    slotInterval: Optional[float] = None
    minimumBookingNotice: Optional[float] = None
    beforeEventBuffer: Optional[float] = None
    afterEventBuffer: Optional[float] = None
    recurrence: Any
    metadata: dict[str, Any]
    price: float
    currency: str
    lockTimeZoneToggleOnBookingPage: bool
    seatsPerTimeSlot: Optional[float] = None
    forwardParamsSuccessRedirect: bool
    successRedirectUrl: str
    isInstantEvent: bool
    seatsShowAvailabilityCount: Optional[bool] = None
    scheduleId: float
    bookingLimitsCount: Optional[dict[str, Any]] = None
    onlyShowFirstAvailableSlot: Optional[bool] = None
    bookingLimitsDuration: Optional[dict[str, Any]] = None
    bookingWindow: Optional[List[Any]] = None
    bookerLayouts: Optional[dict[str, Any]] = None
    confirmationPolicy: Optional[dict[str, Any]] = None
    requiresBookerEmailVerification: Optional[bool] = None
    hideCalendarNotes: Optional[bool] = None
    color: Optional[dict[str, Any]] = None
    seats: Optional[dict[str, Any]] = None
    offsetStart: Optional[float] = None
    customName: Optional[str] = None
    destinationCalendar: Optional[dict[str, Any]] = None
    useDestinationCalendarEmail: Optional[bool] = None
    hideCalendarEventDetails: Optional[bool] = None
    teamId: float
    ownerId: Optional[float] = None
    parentEventTypeId: Optional[float] = None
    hosts: List[ListeventtypesbyteamandorgresponseDataItemHostsItem]
    assignAllTeamMembers: Optional[bool] = None
    schedulingType: str
    team: dict[str, Any]


class Listeventtypesbyteamandorgresponse(BaseModel):
    status: str
    data: List[ListeventtypesbyteamandorgresponseDataItem]


class Geteventtypesbyteamidresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Createphonecalleventresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Listorganizationmembershipsresponse(BaseModel):
    status: str
    data: dict[str, Any]


class GetorganizationschedulesresponseDataItemAvailabilityItem(BaseModel):
    days: List[str]
    startTime: str
    endTime: str


class GetorganizationschedulesresponseDataItemOverridesItem(BaseModel):
    date: str
    startTime: str
    endTime: str


class GetorganizationschedulesresponseDataItem(BaseModel):
    id: float
    ownerId: float
    name: str
    timeZone: str
    availability: List[GetorganizationschedulesresponseDataItemAvailabilityItem]
    isDefault: bool
    overrides: List[GetorganizationschedulesresponseDataItemOverridesItem]


class Getorganizationschedulesresponse(BaseModel):
    status: str
    data: List[GetorganizationschedulesresponseDataItem]
    error: Optional[dict[str, Any]] = None


class Createuserscheduleresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Getscheduledetailresponse(BaseModel):
    status: str
    data: Any
    error: Optional[dict[str, Any]] = None


class Updateuserschedulebyidresponse(BaseModel):
    status: str
    data: dict[str, Any]
    error: Optional[dict[str, Any]] = None


class GetorganizationteamsresponseDataItem(BaseModel):
    id: float
    parentId: Optional[float] = None
    name: str
    slug: Optional[str] = None
    logoUrl: Optional[str] = None
    calVideoLogo: Optional[str] = None
    appLogo: Optional[str] = None
    appIconLogo: Optional[str] = None
    bio: Optional[str] = None
    hideBranding: Optional[bool] = None
    isOrganization: bool
    isPrivate: Optional[bool] = None
    hideBookATeamMember: Optional[bool] = None
    metadata: Optional[str] = None
    theme: Optional[str] = None
    brandColor: Optional[str] = None
    darkBrandColor: Optional[str] = None
    bannerUrl: Optional[str] = None
    timeFormat: Optional[float] = None
    timeZone: Optional[str] = None
    weekStart: Optional[str] = None


class Getorganizationteamsresponse(BaseModel):
    status: str
    data: List[GetorganizationteamsresponseDataItem]


class Createteaminorganizationresponse(BaseModel):
    status: str
    data: dict[str, Any]


class ListteammembershipsresponseDataItem(BaseModel):
    id: float
    userId: float
    teamId: float
    accepted: bool
    role: str
    disableImpersonation: Optional[bool] = None
    user: dict[str, Any]


class Listteammembershipsresponse(BaseModel):
    status: str
    data: List[ListteammembershipsresponseDataItem]


class Createteammembershipresponse(BaseModel):
    status: str
    data: dict[str, Any]


class ListorgusersresponseDataItem(BaseModel):
    id: float
    username: Optional[str] = None
    name: Optional[str] = None
    email: str
    emailVerified: Optional[str] = None
    bio: Optional[str] = None
    avatarUrl: Optional[str] = None
    timeZone: str
    weekStart: str
    appTheme: Optional[str] = None
    theme: Optional[str] = None
    defaultScheduleId: Optional[float] = None
    locale: Optional[str] = None
    timeFormat: Optional[float] = None
    hideBranding: bool
    brandColor: Optional[str] = None
    darkBrandColor: Optional[str] = None
    allowDynamicBooking: Optional[bool] = None
    createdDate: str
    verified: Optional[bool] = None
    invitedTo: Optional[float] = None
    profile: Any


class Listorgusersresponse(BaseModel):
    status: str
    data: List[ListorgusersresponseDataItem]


class Createorguserresponse(BaseModel):
    status: str
    data: dict[str, Any]


class GetorgwebhooksresponseDataItem(BaseModel):
    payloadTemplate: str
    teamId: float
    id: float
    triggers: List[dict[str, Any]]
    subscriberUrl: str
    active: bool
    secret: Optional[str] = None


class Getorgwebhooksresponse(BaseModel):
    status: str
    data: List[GetorgwebhooksresponseDataItem]


class Createwebhookresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Listbookingsresponse(BaseModel):
    status: str
    data: List[Any]
    error: Optional[dict[str, Any]] = None


class Getbookingbyuidresponse(BaseModel):
    status: str
    data: Any
    error: Optional[dict[str, Any]] = None


class Reschedulebookingbyuidresponse(BaseModel):
    status: str
    data: Any


class Cancelbookingbyuidresponse(BaseModel):
    status: str
    data: Any


class Markbookingabsentbyuidresponse(BaseModel):
    status: str
    data: Any


class Reassignbookingresponse(BaseModel):
    status: str
    data: Any


class Saveicsfeedpostresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Checkicsfeedresponse(BaseModel):
    pass


class GetcalendarsbusytimesresponseDataItem(BaseModel):
    start: str
    end: str
    source: Optional[str] = None


class Getcalendarsbusytimesresponse(BaseModel):
    status: str
    data: List[GetcalendarsbusytimesresponseDataItem]


class Getcalendarsresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Disconnectcalendarresponse(BaseModel):
    status: str
    data: dict[str, Any]


class ConferencingcontrollerConnectresponse(BaseModel):
    status: str
    data: dict[str, Any]


class ListconferencingresponseDataItem(BaseModel):
    id: float
    type: str
    userId: float
    invalid: Optional[bool] = None


class Listconferencingresponse(BaseModel):
    status: str
    data: List[ListconferencingresponseDataItem]


class Getdefaultconferencingresponse(BaseModel):
    status: str
    data: Optional[dict[str, Any]] = None


class Updatedestinationcalendarsresponse(BaseModel):
    status: str
    data: dict[str, Any]


class ListeventtypesresponseDataItem(BaseModel):
    id: float
    lengthInMinutes: float
    lengthInMinutesOptions: Optional[List[float]] = None
    title: str
    slug: str
    description: str
    locations: List[Any]
    bookingFields: List[Any]
    disableGuests: bool
    slotInterval: Optional[dict[str, Any]] = None
    minimumBookingNotice: Optional[float] = None
    beforeEventBuffer: Optional[float] = None
    afterEventBuffer: Optional[float] = None
    recurrence: Any
    metadata: dict[str, Any]
    price: float
    currency: str
    lockTimeZoneToggleOnBookingPage: bool
    seatsPerTimeSlot: Optional[dict[str, Any]] = None
    forwardParamsSuccessRedirect: dict[str, Any]
    successRedirectUrl: dict[str, Any]
    isInstantEvent: bool
    seatsShowAvailabilityCount: Optional[bool] = None
    scheduleId: float
    bookingLimitsCount: Optional[dict[str, Any]] = None
    onlyShowFirstAvailableSlot: Optional[bool] = None
    bookingLimitsDuration: Optional[dict[str, Any]] = None
    bookingWindow: Optional[List[Any]] = None
    bookerLayouts: Optional[dict[str, Any]] = None
    confirmationPolicy: Optional[dict[str, Any]] = None
    requiresBookerEmailVerification: Optional[bool] = None
    hideCalendarNotes: Optional[bool] = None
    color: Optional[dict[str, Any]] = None
    seats: Optional[dict[str, Any]] = None
    offsetStart: Optional[float] = None
    customName: Optional[str] = None
    destinationCalendar: Optional[dict[str, Any]] = None
    useDestinationCalendarEmail: Optional[bool] = None
    hideCalendarEventDetails: Optional[bool] = None
    ownerId: float
    users: List[str]


class Listeventtypesresponse(BaseModel):
    status: str
    data: List[ListeventtypesresponseDataItem]


class Geteventtypebyidresponse(BaseModel):
    status: str
    data: Any


class Deleteeventtypebyidresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Createeventtypewebhookresponse(BaseModel):
    status: str
    data: dict[str, Any]


class GeteventwebhooksresponseDataItem(BaseModel):
    payloadTemplate: str
    eventTypeId: float
    id: float
    triggers: List[dict[str, Any]]
    subscriberUrl: str
    active: bool
    secret: Optional[str] = None


class Geteventwebhooksresponse(BaseModel):
    status: str
    data: List[GeteventwebhooksresponseDataItem]


class MecontrollerGetmeresponse(BaseModel):
    status: str
    data: dict[str, Any]


class SlotscontrollerReserveslotresponse(BaseModel):
    status: Optional[str] = None
    data: Optional[dict[str, Any]] = None


class Deleteselectedslotresponse(BaseModel):
    status: Optional[str] = None


class Listavailableslotsresponse(BaseModel):
    status: Optional[str] = None
    data: Optional[dict[str, Any]] = None


class StripecontrollerCheckresponse(BaseModel):
    status: str


class TeamscontrollerCreateteamresponse(BaseModel):
    status: str
    data: Any


class Deleteteameventtypebyidresponse(BaseModel):
    status: str
    data: dict[str, Any]


class Createandconfigurewebhookresponse(BaseModel):
    status: str
    data: dict[str, Any]


class WebhookscontrollerGetwebhooksresponseDataItem(BaseModel):
    payloadTemplate: str
    userId: float
    id: float
    triggers: List[dict[str, Any]]
    subscriberUrl: str
    active: bool
    secret: Optional[str] = None


class WebhookscontrollerGetwebhooksresponse(BaseModel):
    status: str
    data: List[WebhookscontrollerGetwebhooksresponseDataItem]
