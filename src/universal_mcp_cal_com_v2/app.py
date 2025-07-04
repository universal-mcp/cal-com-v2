from typing import Any, Optional, List
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
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


class CalApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name="cal-com-v2", integration=integration, **kwargs)
        self.base_url = "https://api.cal.com"

    def get_provider_details(self, clientId: str) -> Getproviderdetailsresponse:
        """
        Retrieves information for a provider using the client ID provided in the path.

        Args:
            clientId (string): clientId

        Returns:
            Getproviderdetailsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Cal Provider
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        url = f"{self.base_url}/v2/provider/{clientId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getproviderdetailsresponse.model_validate(
            self._handle_response(response)
        )

    def get_provider_access_token(
        self, clientId: str
    ) -> Getprovideraccesstokenresponse:
        """
        Retrieves an access token for the specified client ID using a GET request.

        Args:
            clientId (string): clientId

        Returns:
            Getprovideraccesstokenresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Cal Provider
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        url = f"{self.base_url}/v2/provider/{clientId}/access-token"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getprovideraccesstokenresponse.model_validate(
            self._handle_response(response)
        )

    def gcal_controller_redirect(self) -> GcalcontrollerRedirectresponse:
        """
        Retrieves and returns an authorization URL for Google Calendar OAuth using the "GET" method at the "/v2/gcal/oauth/auth-url" path.

        Returns:
            GcalcontrollerRedirectresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Google Calendar
        """
        url = f"{self.base_url}/v2/gcal/oauth/auth-url"
        query_params = {}
        response = self._get(url, params=query_params)
        return GcalcontrollerRedirectresponse.model_validate(
            self._handle_response(response)
        )

    def gcal_controller_save(self, state: str, code: str) -> GcalcontrollerSaveresponse:
        """
        Handles Google Calendar OAuth 2.0 authorization callback by exchanging an authorization code for an access token and saving credentials.

        Args:
            state (string): A unique value used to prevent cross-site request forgery (CSRF) attacks, typically generated by the client and verified by the server during the OAuth flow.
            code (string): Authorization code received from Google Calendar OAuth flow, used to exchange for an access token during the authentication process.

        Returns:
            GcalcontrollerSaveresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Google Calendar
        """
        url = f"{self.base_url}/v2/gcal/oauth/save"
        query_params = {
            k: v for k, v in [("state", state), ("code", code)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GcalcontrollerSaveresponse.model_validate(
            self._handle_response(response)
        )

    def gcal_controller_check(self) -> Getprovideraccesstokenresponse:
        """
        Checks the Google Calendar availability or status using the v2 API and returns a success response if valid.

        Returns:
            Getprovideraccesstokenresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Google Calendar
        """
        url = f"{self.base_url}/v2/gcal/check"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getprovideraccesstokenresponse.model_validate(
            self._handle_response(response)
        )

    def list_client_users(
        self, clientId: str, limit: Optional[float] = None
    ) -> Listclientusersresponse:
        """
        Retrieves a list of users associated with a specific OAuth client ID, optionally limited by the specified query parameter.

        Args:
            clientId (string): clientId
            limit (number): The number of items to return Example: '10'.

        Returns:
            Listclientusersresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Managed Users
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        url = f"{self.base_url}/v2/oauth-clients/{clientId}/users"
        query_params = {k: v for k, v in [("limit", limit)] if v is not None}
        response = self._get(url, params=query_params)
        return Listclientusersresponse.model_validate(self._handle_response(response))

    def create_oauth_client_user(
        self,
        clientId: str,
        email: str,
        name: str,
        timeFormat: Optional[float] = None,
        weekStart: Optional[str] = None,
        timeZone: Optional[str] = None,
        locale: Optional[str] = None,
        avatarUrl: Optional[str] = None,
    ) -> Createoauthclientuserresponse:
        """
        Creates a new user for an OAuth client specified by the `clientId` and returns a successful response with a 201 status code.

        Args:
            clientId (string): clientId
            email (string): email Example: 'alice@example.com'.
            name (string): Managed user's name is used in emails Example: 'Alice Smith'.
            timeFormat (number): Must be a number 12 or 24 Example: '12'.
            weekStart (string): weekStart Example: 'Monday'.
            timeZone (string): Timezone is used to create user's default schedule from Monday to Friday from 9AM to 5PM. If it is not passed then user does not have
              a default schedule and it must be created manually via the /schedules endpoint. Until the schedule is created, the user can't access availability atom to set his / her availability nor booked.
              It will default to Europe/London if not passed. Example: 'America/New_York'.
            locale (string): locale Example: 'en'.
            avatarUrl (string): URL of the user's avatar image Example: 'https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png'.

        Returns:
            Createoauthclientuserresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Managed Users
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        request_body_data = None
        request_body_data = {
            "email": email,
            "name": name,
            "timeFormat": timeFormat,
            "weekStart": weekStart,
            "timeZone": timeZone,
            "locale": locale,
            "avatarUrl": avatarUrl,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/oauth-clients/{clientId}/users"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createoauthclientuserresponse.model_validate(
            self._handle_response(response)
        )

    def get_oauth_client_user_by_id(
        self, clientId: str, userId: str
    ) -> Getoauthclientuserbyidresponse:
        """
        Retrieves user-specific information associated with an OAuth client using the provided client ID and user ID.

        Args:
            clientId (string): clientId
            userId (string): userId

        Returns:
            Getoauthclientuserbyidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Managed Users
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v2/oauth-clients/{clientId}/users/{userId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getoauthclientuserbyidresponse.model_validate(
            self._handle_response(response)
        )

    def patch_oauth_client_user_by_id(
        self,
        clientId: str,
        userId: str,
        email: Optional[str] = None,
        name: Optional[str] = None,
        timeFormat: Optional[float] = None,
        defaultScheduleId: Optional[float] = None,
        weekStart: Optional[str] = None,
        timeZone: Optional[str] = None,
        locale: Optional[str] = None,
        avatarUrl: Optional[str] = None,
    ) -> Getoauthclientuserbyidresponse:
        """
        Updates the association of a user with a specified OAuth client using the PATCH method on the "/v2/oauth-clients/{clientId}/users/{userId}" path.

        Args:
            clientId (string): clientId
            userId (string): userId
            email (string): email
            name (string): name
            timeFormat (number): Must be 12 or 24 Example: '12'.
            defaultScheduleId (number): defaultScheduleId
            weekStart (string): weekStart Example: 'Monday'.
            timeZone (string): timeZone
            locale (string): locale Example: 'en'.
            avatarUrl (string): URL of the user's avatar image Example: 'https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png'.

        Returns:
            Getoauthclientuserbyidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Managed Users
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        request_body_data = {
            "email": email,
            "name": name,
            "timeFormat": timeFormat,
            "defaultScheduleId": defaultScheduleId,
            "weekStart": weekStart,
            "timeZone": timeZone,
            "locale": locale,
            "avatarUrl": avatarUrl,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/oauth-clients/{clientId}/users/{userId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Getoauthclientuserbyidresponse.model_validate(
            self._handle_response(response)
        )

    def delete_user_by_client_id_id(
        self, clientId: str, userId: str
    ) -> Getoauthclientuserbyidresponse:
        """
        Removes a user's association with an OAuth client identified by the client ID and user ID.

        Args:
            clientId (string): clientId
            userId (string): userId

        Returns:
            Getoauthclientuserbyidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Managed Users
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v2/oauth-clients/{clientId}/users/{userId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Getoauthclientuserbyidresponse.model_validate(
            self._handle_response(response)
        )

    def force_refresh_user(
        self, clientId: str, userId: str
    ) -> Forcerefreshuserresponse:
        """
        Forces a refresh for the OAuth client's user session, invalidating existing tokens and generating new ones.

        Args:
            clientId (string): clientId
            userId (string): userId

        Returns:
            Forcerefreshuserresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Managed Users
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        url = (
            f"{self.base_url}/v2/oauth-clients/{clientId}/users/{userId}/force-refresh"
        )
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Forcerefreshuserresponse.model_validate(self._handle_response(response))

    def refresh_oauth_client_token(
        self, clientId: str, refreshToken: str
    ) -> Forcerefreshuserresponse:
        """
        Refreshes an access token for a specified client using OAuth 2.0, allowing the client to obtain a new access token without user interaction.

        Args:
            clientId (string): clientId
            refreshToken (string): Managed user's refresh token.

        Returns:
            Forcerefreshuserresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Managed Users
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        request_body_data = None
        request_body_data = {
            "refreshToken": refreshToken,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/oauth/{clientId}/refresh"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Forcerefreshuserresponse.model_validate(self._handle_response(response))

    def create_oauth_client_webhook(
        self,
        clientId: str,
        active: bool,
        subscriberUrl: str,
        triggers: str,
        payloadTemplate: Optional[str] = None,
        secret: Optional[str] = None,
    ) -> Createoauthclientwebhookresponse:
        """
        Creates a webhook for an OAuth client using the client ID specified in the path, enabling event-driven communication.

        Args:
            clientId (string): clientId
            active (boolean): active
            subscriberUrl (string): subscriberUrl
            triggers (string): triggers Example: "['BOOKING_CREATED', 'BOOKING_RESCHEDULED', 'BOOKING_CANCELLED', 'BOOKING_CONFIRMED', 'BOOKING_REJECTED', 'BOOKING_COMPLETED', 'BOOKING_NO_SHOW', 'BOOKING_REOPENED']".
            payloadTemplate (string): The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information Example: '{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}'.
            secret (string): secret

        Returns:
            Createoauthclientwebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Webhooks
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        request_body_data = None
        request_body_data = {
            "payloadTemplate": payloadTemplate,
            "active": active,
            "subscriberUrl": subscriberUrl,
            "triggers": triggers,
            "secret": secret,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/oauth-clients/{clientId}/webhooks"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createoauthclientwebhookresponse.model_validate(
            self._handle_response(response)
        )

    def list_webhooks_by_client_id(
        self, clientId: str, take: Optional[float] = None, skip: Optional[float] = None
    ) -> Listwebhooksbyclientidresponse:
        """
        Retrieves a paginated list of webhooks associated with a specific OAuth client using clientId, take, and skip parameters for pagination.

        Args:
            clientId (string): clientId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Listwebhooksbyclientidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Webhooks
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        url = f"{self.base_url}/v2/oauth-clients/{clientId}/webhooks"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Listwebhooksbyclientidresponse.model_validate(
            self._handle_response(response)
        )

    def delete_client_webhook(self, clientId: str) -> Deleteclientwebhookresponse:
        """
        Deletes a webhook associated with an OAuth client identified by the provided client ID using the DELETE method.

        Args:
            clientId (string): clientId

        Returns:
            Deleteclientwebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Webhooks
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        url = f"{self.base_url}/v2/oauth-clients/{clientId}/webhooks"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Deleteclientwebhookresponse.model_validate(
            self._handle_response(response)
        )

    def update_webhook(
        self,
        clientId: str,
        webhookId: str,
        payloadTemplate: Optional[str] = None,
        active: Optional[bool] = None,
        subscriberUrl: Optional[str] = None,
        triggers: Optional[str] = None,
        secret: Optional[str] = None,
    ) -> Createoauthclientwebhookresponse:
        """
        Updates an existing webhook for a specified OAuth client using the "PATCH" method, modifying its configuration as needed.

        Args:
            clientId (string): clientId
            webhookId (string): webhookId
            payloadTemplate (string): The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information Example: '{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}'.
            active (boolean): active
            subscriberUrl (string): subscriberUrl
            triggers (string): triggers Example: "['BOOKING_CREATED', 'BOOKING_RESCHEDULED', 'BOOKING_CANCELLED', 'BOOKING_CONFIRMED', 'BOOKING_REJECTED', 'BOOKING_COMPLETED', 'BOOKING_NO_SHOW', 'BOOKING_REOPENED']".
            secret (string): secret

        Returns:
            Createoauthclientwebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Webhooks
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        request_body_data = None
        request_body_data = {
            "payloadTemplate": payloadTemplate,
            "active": active,
            "subscriberUrl": subscriberUrl,
            "triggers": triggers,
            "secret": secret,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/oauth-clients/{clientId}/webhooks/{webhookId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Createoauthclientwebhookresponse.model_validate(
            self._handle_response(response)
        )

    def get_oauth_client_webhook_by_id(
        self, clientId: str, webhookId: str
    ) -> Createoauthclientwebhookresponse:
        """
        Retrieves information about a specific webhook associated with an OAuth client using the "GET" method at the specified path.

        Args:
            clientId (string): clientId
            webhookId (string): webhookId

        Returns:
            Createoauthclientwebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Webhooks
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        url = f"{self.base_url}/v2/oauth-clients/{clientId}/webhooks/{webhookId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Createoauthclientwebhookresponse.model_validate(
            self._handle_response(response)
        )

    def delete_oauth_client_webhook_by_id(
        self, clientId: str, webhookId: str
    ) -> Createoauthclientwebhookresponse:
        """
        Deletes a webhook associated with a specific OAuth client using the provided client and webhook IDs.

        Args:
            clientId (string): clientId
            webhookId (string): webhookId

        Returns:
            Createoauthclientwebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Platform / Webhooks
        """
        if clientId is None:
            raise ValueError("Missing required parameter 'clientId'.")
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        url = f"{self.base_url}/v2/oauth-clients/{clientId}/webhooks/{webhookId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Createoauthclientwebhookresponse.model_validate(
            self._handle_response(response)
        )

    def list_org_attributes(
        self, orgId: str, take: Optional[float] = None, skip: Optional[float] = None
    ) -> Listorgattributesresponse:
        """
        Retrieves a list of organization attributes filtered by pagination parameters.

        Args:
            orgId (string): orgId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Listorgattributesresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/attributes"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Listorgattributesresponse.model_validate(self._handle_response(response))

    def create_org_attributes(
        self,
        orgId: str,
        name: str,
        slug: str,
        type: str,
        options: List[dict[str, Any]],
        enabled: Optional[bool] = None,
    ) -> Createorgattributesresponse:
        """
        Adds new attributes to an organization using the API, specifying the organization ID in the path, and returns a successful creation status.

        Args:
            orgId (string): orgId
            name (string): name
            slug (string): slug
            type (string): type
            options (array): options
            enabled (boolean): enabled

        Returns:
            Createorgattributesresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "slug": slug,
            "type": type,
            "options": options,
            "enabled": enabled,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/attributes"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createorgattributesresponse.model_validate(
            self._handle_response(response)
        )

    def fetch_organization_attribute_by_id(
        self, orgId: str, attributeId: str
    ) -> Fetchorganizationattributebyidresponse:
        """
        Retrieves a specific attribute for an organization based on the provided orgId and attributeId.

        Args:
            orgId (string): orgId
            attributeId (string): attributeId

        Returns:
            Fetchorganizationattributebyidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if attributeId is None:
            raise ValueError("Missing required parameter 'attributeId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/attributes/{attributeId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Fetchorganizationattributebyidresponse.model_validate(
            self._handle_response(response)
        )

    def update_organization_attribute(
        self,
        orgId: str,
        attributeId: str,
        name: Optional[str] = None,
        slug: Optional[str] = None,
        type: Optional[str] = None,
        enabled: Optional[bool] = None,
    ) -> Createorgattributesresponse:
        """
        Modifies an attribute of an organization using the PATCH method, updating the specified attribute by ID within the given organization.

        Args:
            orgId (string): orgId
            attributeId (string): attributeId
            name (string): name
            slug (string): slug
            type (string): type
            enabled (boolean): enabled

        Returns:
            Createorgattributesresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if attributeId is None:
            raise ValueError("Missing required parameter 'attributeId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "slug": slug,
            "type": type,
            "enabled": enabled,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/attributes/{attributeId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Createorgattributesresponse.model_validate(
            self._handle_response(response)
        )

    def delete_org_attribute(
        self, orgId: str, attributeId: str
    ) -> Createorgattributesresponse:
        """
        Deletes a specified attribute from an organization using the provided orgId and attributeId path parameters.

        Args:
            orgId (string): orgId
            attributeId (string): attributeId

        Returns:
            Createorgattributesresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if attributeId is None:
            raise ValueError("Missing required parameter 'attributeId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/attributes/{attributeId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Createorgattributesresponse.model_validate(
            self._handle_response(response)
        )

    def create_org_attribute_option(
        self, orgId: str, attributeId: str, value: str, slug: str
    ) -> Createorgattributeoptionresponse:
        """
        Creates a new option for the specified attribute in the given organization and returns the created resource.

        Args:
            orgId (string): orgId
            attributeId (string): attributeId
            value (string): value
            slug (string): slug

        Returns:
            Createorgattributeoptionresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes / Options
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if attributeId is None:
            raise ValueError("Missing required parameter 'attributeId'.")
        request_body_data = None
        request_body_data = {
            "value": value,
            "slug": slug,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = (
            f"{self.base_url}/v2/organizations/{orgId}/attributes/{attributeId}/options"
        )
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createorgattributeoptionresponse.model_validate(
            self._handle_response(response)
        )

    def get_org_attribute_options(
        self, orgId: str, attributeId: str
    ) -> Getorgattributeoptionsresponse:
        """
        Retrieves options for a specific attribute within an organization using the "GET" method at the "/v2/organizations/{orgId}/attributes/{attributeId}/options" endpoint.

        Args:
            orgId (string): orgId
            attributeId (string): attributeId

        Returns:
            Getorgattributeoptionsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes / Options
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if attributeId is None:
            raise ValueError("Missing required parameter 'attributeId'.")
        url = (
            f"{self.base_url}/v2/organizations/{orgId}/attributes/{attributeId}/options"
        )
        query_params = {}
        response = self._get(url, params=query_params)
        return Getorgattributeoptionsresponse.model_validate(
            self._handle_response(response)
        )

    def delete_attribute_option_by_id(
        self, orgId: str, attributeId: str, optionId: str
    ) -> Createorgattributeoptionresponse:
        """
        Deletes a specific attribute option for an organization's custom attributes using the provided orgId, attributeId, and optionId.

        Args:
            orgId (string): orgId
            attributeId (string): attributeId
            optionId (string): optionId

        Returns:
            Createorgattributeoptionresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes / Options
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if attributeId is None:
            raise ValueError("Missing required parameter 'attributeId'.")
        if optionId is None:
            raise ValueError("Missing required parameter 'optionId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Createorgattributeoptionresponse.model_validate(
            self._handle_response(response)
        )

    def patch_option_by_id(
        self,
        orgId: str,
        attributeId: str,
        optionId: str,
        value: Optional[str] = None,
        slug: Optional[str] = None,
    ) -> Createorgattributeoptionresponse:
        """
        Updates a specific option for an organization's attribute using partial modifications.

        Args:
            orgId (string): orgId
            attributeId (string): attributeId
            optionId (string): optionId
            value (string): value
            slug (string): slug

        Returns:
            Createorgattributeoptionresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes / Options
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if attributeId is None:
            raise ValueError("Missing required parameter 'attributeId'.")
        if optionId is None:
            raise ValueError("Missing required parameter 'optionId'.")
        request_body_data = None
        request_body_data = {
            "value": value,
            "slug": slug,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/attributes/{attributeId}/options/{optionId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Createorgattributeoptionresponse.model_validate(
            self._handle_response(response)
        )

    def set_user_attribute_option(
        self,
        orgId: str,
        userId: str,
        attributeId: str,
        value: Optional[str] = None,
        attributeOptionId: Optional[str] = None,
    ) -> Setuserattributeoptionresponse:
        """
        Assigns attribute options to a user within an organization using the POST method and returns a creation status.

        Args:
            orgId (string): orgId
            userId (string): userId
            attributeId (string): attributeId
            value (string): value
            attributeOptionId (string): attributeOptionId

        Returns:
            Setuserattributeoptionresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes / Options
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        request_body_data = {
            "value": value,
            "attributeOptionId": attributeOptionId,
            "attributeId": attributeId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/attributes/options/{userId}"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Setuserattributeoptionresponse.model_validate(
            self._handle_response(response)
        )

    def get_user_org_attribute_options(
        self, orgId: str, userId: str
    ) -> Getuserorgattributeoptionsresponse:
        """
        Retrieves attribute options for a specified user within an organization using the "GET" method.

        Args:
            orgId (string): orgId
            userId (string): userId

        Returns:
            Getuserorgattributeoptionsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes / Options
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/attributes/options/{userId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getuserorgattributeoptionsresponse.model_validate(
            self._handle_response(response)
        )

    def delete_attribute_option(
        self, orgId: str, userId: str, attributeOptionId: str
    ) -> Setuserattributeoptionresponse:
        """
        Deletes a specific attribute option for a user within an organization via the provided path parameters.

        Args:
            orgId (string): orgId
            userId (string): userId
            attributeOptionId (string): attributeOptionId

        Returns:
            Setuserattributeoptionresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Attributes / Options
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        if attributeOptionId is None:
            raise ValueError("Missing required parameter 'attributeOptionId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/attributes/options/{userId}/{attributeOptionId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Setuserattributeoptionresponse.model_validate(
            self._handle_response(response)
        )

    def create_event_type(
        self,
        orgId: str,
        teamId: str,
        lengthInMinutes: float,
        lengthInMinutesOptions: List[str],
        title: str,
        slug: str,
        schedulingType: dict[str, Any],
        hosts: List[dict[str, Any]],
        description: Optional[str] = None,
        locations: Optional[List[Any]] = None,
        bookingFields: Optional[List[Any]] = None,
        disableGuests: Optional[bool] = None,
        slotInterval: Optional[float] = None,
        minimumBookingNotice: Optional[float] = None,
        beforeEventBuffer: Optional[float] = None,
        afterEventBuffer: Optional[float] = None,
        scheduleId: Optional[float] = None,
        bookingLimitsCount: Optional[Any] = None,
        onlyShowFirstAvailableSlot: Optional[bool] = None,
        bookingLimitsDuration: Optional[Any] = None,
        bookingWindow: Optional[Any] = None,
        offsetStart: Optional[float] = None,
        bookerLayouts: Optional[Any] = None,
        confirmationPolicy: Optional[Any] = None,
        recurrence: Optional[Any] = None,
        requiresBookerEmailVerification: Optional[bool] = None,
        hideCalendarNotes: Optional[bool] = None,
        lockTimeZoneToggleOnBookingPage: Optional[bool] = None,
        color: Optional[dict[str, Any]] = None,
        seats: Optional[Any] = None,
        customName: Optional[str] = None,
        destinationCalendar: Optional[dict[str, Any]] = None,
        useDestinationCalendarEmail: Optional[bool] = None,
        hideCalendarEventDetails: Optional[bool] = None,
        successRedirectUrl: Optional[str] = None,
        assignAllTeamMembers: Optional[bool] = None,
    ) -> Createeventtyperesponse:
        """
        Creates a new event type within a specified team and organization.

        Args:
            orgId (string): orgId
            teamId (string): teamId
            lengthInMinutes (number): lengthInMinutes Example: '60'.
            lengthInMinutesOptions (array): If you want that user can choose between different lengths of the event you can specify them here. Must include the provided `lengthInMinutes`. Example: '[15, 30, 60]'.
            title (string): title Example: 'Learn the secrets of masterchief!'.
            slug (string): slug Example: 'learn-the-secrets-of-masterchief'.
            schedulingType (object): schedulingType
            hosts (array): hosts
            description (string): description Example: 'Discover the culinary wonders of the Argentina by making the best flan ever!'.
            locations (array): Locations where the event will take place. If not provided, cal video link will be used as the location.
            bookingFields (array): Custom fields that can be added to the booking form when the event is booked by someone. By default booking form has name and email field.
            disableGuests (boolean): If true, person booking this event't cant add guests via their emails.
            slotInterval (number): Number representing length of each slot when event is booked. By default it equal length of the event type.
              If event length is 60 minutes then we would have slots 9AM, 10AM, 11AM etc. but if it was changed to 30 minutes then
              we would have slots 9AM, 9:30AM, 10AM, 10:30AM etc. as the available times to book the 60 minute event.
            minimumBookingNotice (number): Minimum number of minutes before the event that a booking can be made.
            beforeEventBuffer (number): Time spaces that can be pre-pended before an event to give more time before it.
            afterEventBuffer (number): Time spaces that can be appended after an event to give more time after it.
            scheduleId (number): If you want that this event has different schedule than user's default one you can specify it here.
            bookingLimitsCount (string): Limit how many times this event can be booked
            onlyShowFirstAvailableSlot (boolean): This will limit your availability for this event type to one slot per day, scheduled at the earliest available time.
            bookingLimitsDuration (string): Limit total amount of time that this event can be booked
            bookingWindow (string): Limit how far in the future this event can be booked
            offsetStart (number): Offset timeslots shown to bookers by a specified number of minutes
            bookerLayouts (string): Should booker have week, month or column view. Specify default layout and enabled layouts user can pick.
            confirmationPolicy (string): Specify how the booking needs to be manually confirmed before it is pushed to the integrations and a confirmation mail is sent.
            recurrence (string): Create a recurring event type.
            requiresBookerEmailVerification (boolean): requiresBookerEmailVerification
            hideCalendarNotes (boolean): hideCalendarNotes
            lockTimeZoneToggleOnBookingPage (boolean): lockTimeZoneToggleOnBookingPage
            color (object): color
            seats (string): Create an event type with multiple seats.
            customName (string): Customizable event name with valid variables:
              {Event type title}, {Organiser}, {Scheduler}, {Location}, {Organiser first name},
              {Scheduler first name}, {Scheduler last name}, {Event duration}, {LOCATION},
              {HOST/ATTENDEE}, {HOST}, {ATTENDEE}, {USER} Example: '{Event type title} between {Organiser} and {Scheduler}'.
            destinationCalendar (object): destinationCalendar
            useDestinationCalendarEmail (boolean): useDestinationCalendarEmail
            hideCalendarEventDetails (boolean): hideCalendarEventDetails
            successRedirectUrl (string): A valid URL where the booker will redirect to, once the booking is completed successfully Example: 'https://masterchief.com/argentina/flan/video/9129412'.
            assignAllTeamMembers (boolean): If true, all current and future team members will be assigned to this event type

        Returns:
            Createeventtyperesponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Event Types
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        request_body_data = None
        request_body_data = {
            "lengthInMinutes": lengthInMinutes,
            "lengthInMinutesOptions": lengthInMinutesOptions,
            "title": title,
            "slug": slug,
            "description": description,
            "locations": locations,
            "bookingFields": bookingFields,
            "disableGuests": disableGuests,
            "slotInterval": slotInterval,
            "minimumBookingNotice": minimumBookingNotice,
            "beforeEventBuffer": beforeEventBuffer,
            "afterEventBuffer": afterEventBuffer,
            "scheduleId": scheduleId,
            "bookingLimitsCount": bookingLimitsCount,
            "onlyShowFirstAvailableSlot": onlyShowFirstAvailableSlot,
            "bookingLimitsDuration": bookingLimitsDuration,
            "bookingWindow": bookingWindow,
            "offsetStart": offsetStart,
            "bookerLayouts": bookerLayouts,
            "confirmationPolicy": confirmationPolicy,
            "recurrence": recurrence,
            "requiresBookerEmailVerification": requiresBookerEmailVerification,
            "hideCalendarNotes": hideCalendarNotes,
            "lockTimeZoneToggleOnBookingPage": lockTimeZoneToggleOnBookingPage,
            "color": color,
            "seats": seats,
            "customName": customName,
            "destinationCalendar": destinationCalendar,
            "useDestinationCalendarEmail": useDestinationCalendarEmail,
            "hideCalendarEventDetails": hideCalendarEventDetails,
            "successRedirectUrl": successRedirectUrl,
            "schedulingType": schedulingType,
            "hosts": hosts,
            "assignAllTeamMembers": assignAllTeamMembers,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}/event-types"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createeventtyperesponse.model_validate(self._handle_response(response))

    def list_event_types_by_team_and_org(
        self, orgId: str, teamId: str, eventSlug: Optional[str] = None
    ) -> Listeventtypesbyteamandorgresponse:
        """
        Retrieves event types for a specific team within an organization using the "GET" method at the "/v2/organizations/{orgId}/teams/{teamId}/event-types" endpoint, optionally filtering by event slug.

        Args:
            orgId (string): orgId
            teamId (string): teamId
            eventSlug (string): Slug of team event type to return.

        Returns:
            Listeventtypesbyteamandorgresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Event Types
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}/event-types"
        query_params = {k: v for k, v in [("eventSlug", eventSlug)] if v is not None}
        response = self._get(url, params=query_params)
        return Listeventtypesbyteamandorgresponse.model_validate(
            self._handle_response(response)
        )

    def get_event_types_by_team_id(
        self, orgId: str, teamId: str, eventTypeId: str
    ) -> Geteventtypesbyteamidresponse:
        """
        Retrieves details about a specific event type within a team of an organization using the provided organization ID, team ID, and event type ID.

        Args:
            orgId (string): orgId
            teamId (string): teamId
            eventTypeId (string): eventTypeId

        Returns:
            Geteventtypesbyteamidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Event Types
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Geteventtypesbyteamidresponse.model_validate(
            self._handle_response(response)
        )

    def create_phone_call_event(
        self,
        orgId: str,
        teamId: str,
        eventTypeId: str,
        yourPhoneNumber: str,
        numberToCall: str,
        calApiKey: str,
        enabled: dict[str, Any],
        templateType: str,
        schedulerName: Optional[str] = None,
        guestName: Optional[str] = None,
        guestEmail: Optional[str] = None,
        guestCompany: Optional[str] = None,
        beginMessage: Optional[str] = None,
        generalPrompt: Optional[str] = None,
    ) -> Createphonecalleventresponse:
        """
        Initiates a phone call for a specific event type under an organization's team context and returns a 201 Created response upon successful creation.

        Args:
            orgId (string): orgId
            teamId (string): teamId
            eventTypeId (string): eventTypeId
            yourPhoneNumber (string): Your phone number
            numberToCall (string): Number to call
            calApiKey (string): CAL API Key
            enabled (object): Enabled status
            templateType (string): Template type
            schedulerName (string): Scheduler name
            guestName (string): Guest name
            guestEmail (string): Guest email
            guestCompany (string): Guest company
            beginMessage (string): Begin message
            generalPrompt (string): General prompt

        Returns:
            Createphonecalleventresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Event Types
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        request_body_data = None
        request_body_data = {
            "yourPhoneNumber": yourPhoneNumber,
            "numberToCall": numberToCall,
            "calApiKey": calApiKey,
            "enabled": enabled,
            "templateType": templateType,
            "schedulerName": schedulerName,
            "guestName": guestName,
            "guestEmail": guestEmail,
            "guestCompany": guestCompany,
            "beginMessage": beginMessage,
            "generalPrompt": generalPrompt,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}/event-types/{eventTypeId}/create-phone-call"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createphonecalleventresponse.model_validate(
            self._handle_response(response)
        )

    def list_event_types_by_org_id(
        self, orgId: str, take: Optional[float] = None, skip: Optional[float] = None
    ) -> Listeventtypesbyteamandorgresponse:
        """
        Retrieves a paginated list of event types for teams within a specified organization.

        Args:
            orgId (string): orgId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Listeventtypesbyteamandorgresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Event Types
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/event-types"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Listeventtypesbyteamandorgresponse.model_validate(
            self._handle_response(response)
        )

    def list_organization_memberships(
        self, orgId: str, take: Optional[float] = None, skip: Optional[float] = None
    ) -> Listorganizationmembershipsresponse:
        """
        Retrieves a list of memberships for an organization identified by the specified `orgId`, allowing pagination through optional `take` and `skip` query parameters.

        Args:
            orgId (string): orgId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Listorganizationmembershipsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Memberships
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/memberships"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Listorganizationmembershipsresponse.model_validate(
            self._handle_response(response)
        )

    def create_membership(
        self,
        orgId: str,
        userId: float,
        role: str,
        accepted: Optional[bool] = None,
        disableImpersonation: Optional[bool] = None,
    ) -> Listorganizationmembershipsresponse:
        """
        Creates a new membership for an organization identified by {orgId} using the API.

        Args:
            orgId (string): orgId
            userId (number): userId
            role (string): role
            accepted (boolean): accepted
            disableImpersonation (boolean): disableImpersonation

        Returns:
            Listorganizationmembershipsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Memberships
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        request_body_data = None
        request_body_data = {
            "userId": userId,
            "accepted": accepted,
            "role": role,
            "disableImpersonation": disableImpersonation,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/memberships"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Listorganizationmembershipsresponse.model_validate(
            self._handle_response(response)
        )

    def get_org_membership_by_id(
        self, orgId: str, membershipId: str
    ) -> Listorganizationmembershipsresponse:
        """
        Retrieves membership details for a specific organization membership using the provided organization ID and membership ID.

        Args:
            orgId (string): orgId
            membershipId (string): membershipId

        Returns:
            Listorganizationmembershipsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Memberships
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if membershipId is None:
            raise ValueError("Missing required parameter 'membershipId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/memberships/{membershipId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Listorganizationmembershipsresponse.model_validate(
            self._handle_response(response)
        )

    def delete_org_membership_by_id(
        self, orgId: str, membershipId: str
    ) -> Listorganizationmembershipsresponse:
        """
        Removes a user's membership from the specified organization by deleting the membership record at the given path.

        Args:
            orgId (string): orgId
            membershipId (string): membershipId

        Returns:
            Listorganizationmembershipsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Memberships
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if membershipId is None:
            raise ValueError("Missing required parameter 'membershipId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/memberships/{membershipId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Listorganizationmembershipsresponse.model_validate(
            self._handle_response(response)
        )

    def update_membership_by_id_org(
        self,
        orgId: str,
        membershipId: str,
        accepted: Optional[bool] = None,
        role: Optional[str] = None,
        disableImpersonation: Optional[bool] = None,
    ) -> Listorganizationmembershipsresponse:
        """
        Updates an organization membership's details using the PATCH method and returns the updated membership data.

        Args:
            orgId (string): orgId
            membershipId (string): membershipId
            accepted (boolean): accepted
            role (string): role
            disableImpersonation (boolean): disableImpersonation

        Returns:
            Listorganizationmembershipsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Memberships
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if membershipId is None:
            raise ValueError("Missing required parameter 'membershipId'.")
        request_body_data = None
        request_body_data = {
            "accepted": accepted,
            "role": role,
            "disableImpersonation": disableImpersonation,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/memberships/{membershipId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Listorganizationmembershipsresponse.model_validate(
            self._handle_response(response)
        )

    def get_organization_schedules(
        self, orgId: str, take: Optional[float] = None, skip: Optional[float] = None
    ) -> Getorganizationschedulesresponse:
        """
        Retrieves a list of schedules for the specified organization, using pagination parameters to limit results.

        Args:
            orgId (string): orgId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Getorganizationschedulesresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Schedules
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/schedules"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Getorganizationschedulesresponse.model_validate(
            self._handle_response(response)
        )

    def create_user_schedule(
        self,
        orgId: str,
        userId: str,
        name: str,
        timeZone: str,
        isDefault: bool,
        availability: Optional[List[dict[str, Any]]] = None,
        overrides: Optional[List[dict[str, Any]]] = None,
    ) -> Createuserscheduleresponse:
        """
        Creates a schedule for the specified user within an organization and returns a success status upon creation.

        Args:
            orgId (string): orgId
            userId (string): userId
            name (string): name Example: 'Catch up hours'.
            timeZone (string): Timezone is used to calculate available times when an event using the schedule is booked. Example: 'Europe/Rome'.
            isDefault (boolean): Each user should have 1 default schedule. If you specified `timeZone` when creating managed user, then the default schedule will be created with that timezone.
            Default schedule means that if an event type is not tied to a specific schedule then the default schedule is used. Example: 'True'.
            availability (array): Each object contains days and times when the user is available. If not passed, the default availability is Monday to Friday from 09:00 to 17:00. Example: "[{'days': ['Monday', 'Tuesday'], 'startTime': '17:00', 'endTime': '19:00'}, {'days': ['Wednesday', 'Thursday'], 'startTime': '16:00', 'endTime': '20:00'}]".
            overrides (array): Need to change availability for a specific date? Add an override. Example: "[{'date': '2024-05-20', 'startTime': '18:00', 'endTime': '21:00'}]".

        Returns:
            Createuserscheduleresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Schedules, Orgs / Users / Schedules
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "timeZone": timeZone,
            "availability": availability,
            "isDefault": isDefault,
            "overrides": overrides,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/users/{userId}/schedules"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createuserscheduleresponse.model_validate(
            self._handle_response(response)
        )

    def get_user_schedule(
        self, orgId: str, userId: str
    ) -> Getorganizationschedulesresponse:
        """
        Retrieves a user's schedule for a specific organization using the GET method.

        Args:
            orgId (string): orgId
            userId (string): userId

        Returns:
            Getorganizationschedulesresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Schedules, Orgs / Users / Schedules
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/users/{userId}/schedules"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getorganizationschedulesresponse.model_validate(
            self._handle_response(response)
        )

    def get_schedule_detail(
        self, orgId: str, userId: str, scheduleId: str
    ) -> Getscheduledetailresponse:
        """
        Retrieves the specified schedule for a user within an organization.

        Args:
            orgId (string): orgId
            userId (string): userId
            scheduleId (string): scheduleId

        Returns:
            Getscheduledetailresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Schedules, Orgs / Users / Schedules
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        if scheduleId is None:
            raise ValueError("Missing required parameter 'scheduleId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getscheduledetailresponse.model_validate(self._handle_response(response))

    def update_user_schedule_by_id(
        self,
        orgId: str,
        userId: str,
        scheduleId: str,
        name: Optional[str] = None,
        timeZone: Optional[str] = None,
        availability: Optional[List[dict[str, Any]]] = None,
        isDefault: Optional[bool] = None,
        overrides: Optional[List[dict[str, Any]]] = None,
    ) -> Updateuserschedulebyidresponse:
        """
        Updates a user's schedule for a specified organization by applying partial modifications to the schedule's details using the PATCH method.

        Args:
            orgId (string): orgId
            userId (string): userId
            scheduleId (string): scheduleId
            name (string): name Example: 'One-on-one coaching'.
            timeZone (string): timeZone Example: 'Europe/Rome'.
            availability (array): availability Example: "[{'days': ['Monday', 'Tuesday'], 'startTime': '09:00', 'endTime': '10:00'}]".
            isDefault (boolean): isDefault Example: 'True'.
            overrides (array): overrides Example: "[{'date': '2024-05-20', 'startTime': '12:00', 'endTime': '14:00'}]".

        Returns:
            Updateuserschedulebyidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Schedules, Orgs / Users / Schedules
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        if scheduleId is None:
            raise ValueError("Missing required parameter 'scheduleId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "timeZone": timeZone,
            "availability": availability,
            "isDefault": isDefault,
            "overrides": overrides,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Updateuserschedulebyidresponse.model_validate(
            self._handle_response(response)
        )

    def delete_user_schedule_by_id(
        self, orgId: str, userId: str, scheduleId: str
    ) -> Getprovideraccesstokenresponse:
        """
        Deletes a specific schedule for a user within an organization and returns a success status.

        Args:
            orgId (string): orgId
            userId (string): userId
            scheduleId (string): scheduleId

        Returns:
            Getprovideraccesstokenresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Schedules, Orgs / Users / Schedules
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        if scheduleId is None:
            raise ValueError("Missing required parameter 'scheduleId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/users/{userId}/schedules/{scheduleId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Getprovideraccesstokenresponse.model_validate(
            self._handle_response(response)
        )

    def get_organization_teams(
        self, orgId: str, take: Optional[float] = None, skip: Optional[float] = None
    ) -> Getorganizationteamsresponse:
        """
        Retrieves a list of teams for a specified organization using the provided orgId, with optional pagination control via take and skip parameters.

        Args:
            orgId (string): orgId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Getorganizationteamsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams, Teams
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/teams"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Getorganizationteamsresponse.model_validate(
            self._handle_response(response)
        )

    def create_team_in_organization(
        self,
        orgId: str,
        name: str,
        slug: Optional[str] = None,
        logoUrl: Optional[str] = None,
        calVideoLogo: Optional[str] = None,
        appLogo: Optional[str] = None,
        appIconLogo: Optional[str] = None,
        bio: Optional[str] = None,
        hideBranding: Optional[bool] = None,
        isPrivate: Optional[bool] = None,
        hideBookATeamMember: Optional[bool] = None,
        metadata: Optional[str] = None,
        theme: Optional[str] = None,
        brandColor: Optional[str] = None,
        darkBrandColor: Optional[str] = None,
        bannerUrl: Optional[str] = None,
        timeFormat: Optional[float] = None,
        timeZone: Optional[str] = None,
        weekStart: Optional[str] = None,
        autoAcceptCreator: Optional[bool] = None,
    ) -> Createteaminorganizationresponse:
        """
        Creates a new team within the specified organization using the provided organization ID and returns a success status upon creation.

        Args:
            orgId (string): orgId
            name (string): Name of the team Example: 'CalTeam'.
            slug (string): Team slug Example: 'caltel'.
            logoUrl (string): URL of the teams logo image Example: 'https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png'.
            calVideoLogo (string): calVideoLogo
            appLogo (string): appLogo
            appIconLogo (string): appIconLogo
            bio (string): bio
            hideBranding (boolean): hideBranding
            isPrivate (boolean): isPrivate
            hideBookATeamMember (boolean): hideBookATeamMember
            metadata (string): metadata
            theme (string): theme
            brandColor (string): brandColor
            darkBrandColor (string): darkBrandColor
            bannerUrl (string): URL of the teams banner image which is shown on booker Example: 'https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png'.
            timeFormat (number): timeFormat
            timeZone (string): Timezone is used to create teams's default schedule from Monday to Friday from 9AM to 5PM. It will default to Europe/London if not passed. Example: 'America/New_York'.
            weekStart (string): weekStart Example: 'Monday'.
            autoAcceptCreator (boolean): autoAcceptCreator

        Returns:
            Createteaminorganizationresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "slug": slug,
            "logoUrl": logoUrl,
            "calVideoLogo": calVideoLogo,
            "appLogo": appLogo,
            "appIconLogo": appIconLogo,
            "bio": bio,
            "hideBranding": hideBranding,
            "isPrivate": isPrivate,
            "hideBookATeamMember": hideBookATeamMember,
            "metadata": metadata,
            "theme": theme,
            "brandColor": brandColor,
            "darkBrandColor": darkBrandColor,
            "bannerUrl": bannerUrl,
            "timeFormat": timeFormat,
            "timeZone": timeZone,
            "weekStart": weekStart,
            "autoAcceptCreator": autoAcceptCreator,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/teams"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createteaminorganizationresponse.model_validate(
            self._handle_response(response)
        )

    def get_organization_team_me(
        self, orgId: str, take: Optional[float] = None, skip: Optional[float] = None
    ) -> Getorganizationteamsresponse:
        """
        Retrieves the teams for the current user within a specified organization using the "GET" method, optionally allowing pagination through query parameters.

        Args:
            orgId (string): orgId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Getorganizationteamsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/me"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Getorganizationteamsresponse.model_validate(
            self._handle_response(response)
        )

    def get_organization_team_by_id(
        self, orgId: str, teamId: str
    ) -> Createteaminorganizationresponse:
        """
        Retrieves information about a specific team within an organization using the organization and team IDs.

        Args:
            orgId (string): orgId
            teamId (string): teamId

        Returns:
            Createteaminorganizationresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Createteaminorganizationresponse.model_validate(
            self._handle_response(response)
        )

    def delete_team_by_id(
        self, orgId: str, teamId: str
    ) -> Createteaminorganizationresponse:
        """
        Deletes a specific team within an organization and returns a success status upon completion.

        Args:
            orgId (string): orgId
            teamId (string): teamId

        Returns:
            Createteaminorganizationresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Createteaminorganizationresponse.model_validate(
            self._handle_response(response)
        )

    def update_team(
        self,
        orgId: str,
        teamId: str,
        name: Optional[str] = None,
        slug: Optional[str] = None,
        logoUrl: Optional[str] = None,
        calVideoLogo: Optional[str] = None,
        appLogo: Optional[str] = None,
        appIconLogo: Optional[str] = None,
        bio: Optional[str] = None,
        hideBranding: Optional[bool] = None,
        isPrivate: Optional[bool] = None,
        hideBookATeamMember: Optional[bool] = None,
        metadata: Optional[str] = None,
        theme: Optional[str] = None,
        brandColor: Optional[str] = None,
        darkBrandColor: Optional[str] = None,
        bannerUrl: Optional[str] = None,
        timeFormat: Optional[float] = None,
        timeZone: Optional[str] = None,
        weekStart: Optional[str] = None,
        bookingLimits: Optional[str] = None,
        includeManagedEventsInLimits: Optional[bool] = None,
    ) -> Createteaminorganizationresponse:
        """
        Updates the specified team properties within an organization using partial modifications.

        Args:
            orgId (string): orgId
            teamId (string): teamId
            name (string): Name of the team Example: 'CalTeam'.
            slug (string): Team slug Example: 'caltel'.
            logoUrl (string): URL of the teams logo image Example: 'https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png'.
            calVideoLogo (string): calVideoLogo
            appLogo (string): appLogo
            appIconLogo (string): appIconLogo
            bio (string): bio
            hideBranding (boolean): hideBranding
            isPrivate (boolean): isPrivate
            hideBookATeamMember (boolean): hideBookATeamMember
            metadata (string): metadata
            theme (string): theme
            brandColor (string): brandColor
            darkBrandColor (string): darkBrandColor
            bannerUrl (string): URL of the teams banner image which is shown on booker Example: 'https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png'.
            timeFormat (number): timeFormat
            timeZone (string): Timezone is used to create teams's default schedule from Monday to Friday from 9AM to 5PM. It will default to Europe/London if not passed. Example: 'America/New_York'.
            weekStart (string): weekStart Example: 'Monday'.
            bookingLimits (string): bookingLimits
            includeManagedEventsInLimits (boolean): includeManagedEventsInLimits

        Returns:
            Createteaminorganizationresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "slug": slug,
            "logoUrl": logoUrl,
            "calVideoLogo": calVideoLogo,
            "appLogo": appLogo,
            "appIconLogo": appIconLogo,
            "bio": bio,
            "hideBranding": hideBranding,
            "isPrivate": isPrivate,
            "hideBookATeamMember": hideBookATeamMember,
            "metadata": metadata,
            "theme": theme,
            "brandColor": brandColor,
            "darkBrandColor": darkBrandColor,
            "bannerUrl": bannerUrl,
            "timeFormat": timeFormat,
            "timeZone": timeZone,
            "weekStart": weekStart,
            "bookingLimits": bookingLimits,
            "includeManagedEventsInLimits": includeManagedEventsInLimits,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Createteaminorganizationresponse.model_validate(
            self._handle_response(response)
        )

    def list_team_memberships(
        self,
        orgId: str,
        teamId: str,
        take: Optional[float] = None,
        skip: Optional[float] = None,
    ) -> Listteammembershipsresponse:
        """
        Retrieves a paginated list of memberships for a specified team within an organization, using path parameters for orgId and teamId, and query parameters for pagination (take and skip).

        Args:
            orgId (string): orgId
            teamId (string): teamId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Listteammembershipsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams / Memberships
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}/memberships"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Listteammembershipsresponse.model_validate(
            self._handle_response(response)
        )

    def create_team_membership(
        self,
        orgId: str,
        teamId: str,
        userId: float,
        role: str,
        accepted: Optional[bool] = None,
        disableImpersonation: Optional[bool] = None,
    ) -> Createteammembershipresponse:
        """
        Adds a member to the specified team within an organization and returns the membership details.

        Args:
            orgId (string): orgId
            teamId (string): teamId
            userId (number): userId
            role (string): role
            accepted (boolean): accepted
            disableImpersonation (boolean): disableImpersonation

        Returns:
            Createteammembershipresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams / Memberships
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        request_body_data = None
        request_body_data = {
            "userId": userId,
            "accepted": accepted,
            "role": role,
            "disableImpersonation": disableImpersonation,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}/memberships"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createteammembershipresponse.model_validate(
            self._handle_response(response)
        )

    def get_membership_details(
        self, orgId: str, teamId: str, membershipId: str
    ) -> Createteammembershipresponse:
        """
        Retrieves a specific membership record for a team within an organization, identified by membership ID, team ID, and organization ID.

        Args:
            orgId (string): orgId
            teamId (string): teamId
            membershipId (string): membershipId

        Returns:
            Createteammembershipresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams / Memberships
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if membershipId is None:
            raise ValueError("Missing required parameter 'membershipId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Createteammembershipresponse.model_validate(
            self._handle_response(response)
        )

    def delete_org_team_membership_by_id(
        self, orgId: str, teamId: str, membershipId: str
    ) -> Createteammembershipresponse:
        """
        Removes a user's team membership in an organization using the specified organization, team, and membership identifiers.

        Args:
            orgId (string): orgId
            teamId (string): teamId
            membershipId (string): membershipId

        Returns:
            Createteammembershipresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams / Memberships
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if membershipId is None:
            raise ValueError("Missing required parameter 'membershipId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Createteammembershipresponse.model_validate(
            self._handle_response(response)
        )

    def patch_team_membership_by_id(
        self,
        orgId: str,
        teamId: str,
        membershipId: str,
        accepted: Optional[bool] = None,
        role: Optional[str] = None,
        disableImpersonation: Optional[bool] = None,
    ) -> Createteammembershipresponse:
        """
        Updates membership details for a specific organization team member using partial modifications and returns a success status.

        Args:
            orgId (string): orgId
            teamId (string): teamId
            membershipId (string): membershipId
            accepted (boolean): accepted
            role (string): role
            disableImpersonation (boolean): disableImpersonation

        Returns:
            Createteammembershipresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams / Memberships
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if membershipId is None:
            raise ValueError("Missing required parameter 'membershipId'.")
        request_body_data = None
        request_body_data = {
            "accepted": accepted,
            "role": role,
            "disableImpersonation": disableImpersonation,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}/memberships/{membershipId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Createteammembershipresponse.model_validate(
            self._handle_response(response)
        )

    def get_schedule_by_user(
        self, orgId: str, teamId: str, userId: str
    ) -> Getorganizationschedulesresponse:
        """
        Retrieves the schedule details for a specific user within a designated team and organization.

        Args:
            orgId (string): orgId
            teamId (string): teamId
            userId (string): userId

        Returns:
            Getorganizationschedulesresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Teams / Schedules, Orgs / Teams / Users / Schedules
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/teams/{teamId}/users/{userId}/schedules"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getorganizationschedulesresponse.model_validate(
            self._handle_response(response)
        )

    def list_org_users(
        self,
        orgId: str,
        take: Optional[float] = None,
        skip: Optional[float] = None,
        emails: Optional[List[str]] = None,
    ) -> Listorgusersresponse:
        """
        Retrieves a list of users for a specified organization, allowing filtering by take, skip, and emails parameters, using the GET method on the "/v2/organizations/{orgId}/users" endpoint.

        Args:
            orgId (string): orgId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.
            emails (array): The email address or an array of email addresses to filter by

        Returns:
            Listorgusersresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Users
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/users"
        query_params = {
            k: v
            for k, v in [("take", take), ("skip", skip), ("emails", emails)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Listorgusersresponse.model_validate(self._handle_response(response))

    def create_org_user(
        self,
        orgId: str,
        email: str,
        username: Optional[str] = None,
        weekday: Optional[str] = None,
        brandColor: Optional[str] = None,
        darkBrandColor: Optional[str] = None,
        hideBranding: Optional[bool] = None,
        timeZone: Optional[str] = None,
        theme: Optional[str] = None,
        appTheme: Optional[str] = None,
        timeFormat: Optional[float] = None,
        defaultScheduleId: Optional[float] = None,
        locale: Optional[str] = None,
        avatarUrl: Optional[str] = None,
        organizationRole: Optional[str] = None,
        autoAccept: Optional[bool] = None,
    ) -> Createorguserresponse:
        """
        Creates a new user within an organization using the provided organization ID.

        Args:
            orgId (string): orgId
            email (string): User email address Example: 'user@example.com'.
            username (string): Username Example: 'user123'.
            weekday (string): Preferred weekday Example: 'Monday'.
            brandColor (string): Brand color in HEX format Example: '#FFFFFF'.
            darkBrandColor (string): Dark brand color in HEX format Example: '#000000'.
            hideBranding (boolean): Hide branding Example: 'False'.
            timeZone (string): Time zone Example: 'America/New_York'.
            theme (string): Theme Example: 'dark'.
            appTheme (string): Application theme Example: 'light'.
            timeFormat (number): Time format Example: '24'.
            defaultScheduleId (number): Default schedule ID Example: '1'.
            locale (string): Locale Example: 'en'.
            avatarUrl (string): Avatar URL Example: 'https://example.com/avatar.jpg'.
            organizationRole (string): organizationRole
            autoAccept (boolean): autoAccept

        Returns:
            Createorguserresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Users
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        request_body_data = None
        request_body_data = {
            "email": email,
            "username": username,
            "weekday": weekday,
            "brandColor": brandColor,
            "darkBrandColor": darkBrandColor,
            "hideBranding": hideBranding,
            "timeZone": timeZone,
            "theme": theme,
            "appTheme": appTheme,
            "timeFormat": timeFormat,
            "defaultScheduleId": defaultScheduleId,
            "locale": locale,
            "avatarUrl": avatarUrl,
            "organizationRole": organizationRole,
            "autoAccept": autoAccept,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/users"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createorguserresponse.model_validate(self._handle_response(response))

    def delete_member_by_id(self, orgId: str, userId: str) -> Createorguserresponse:
        """
        Deletes a user with the specified user ID from an organization identified by the provided organization ID using the DELETE method, returning a status message upon success.

        Args:
            orgId (string): orgId
            userId (string): userId

        Returns:
            Createorguserresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Users
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/users/{userId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Createorguserresponse.model_validate(self._handle_response(response))

    def get_org_webhooks(
        self, orgId: str, take: Optional[float] = None, skip: Optional[float] = None
    ) -> Getorgwebhooksresponse:
        """
        Retrieves a list of webhooks for the specified organization, supporting pagination through skip and take parameters.

        Args:
            orgId (string): orgId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Getorgwebhooksresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Webhooks
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/webhooks"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Getorgwebhooksresponse.model_validate(self._handle_response(response))

    def create_webhook(
        self,
        orgId: str,
        active: bool,
        subscriberUrl: str,
        triggers: str,
        payloadTemplate: Optional[str] = None,
        secret: Optional[str] = None,
    ) -> Createwebhookresponse:
        """
        Creates an organization webhook that triggers HTTP POST payloads for specified events and returns a success status on creation.

        Args:
            orgId (string): orgId
            active (boolean): active
            subscriberUrl (string): subscriberUrl
            triggers (string): triggers Example: "['BOOKING_CREATED', 'BOOKING_RESCHEDULED', 'BOOKING_CANCELLED', 'BOOKING_CONFIRMED', 'BOOKING_REJECTED', 'BOOKING_COMPLETED', 'BOOKING_NO_SHOW', 'BOOKING_REOPENED']".
            payloadTemplate (string): The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information Example: '{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}'.
            secret (string): secret

        Returns:
            Createwebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Webhooks
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        request_body_data = None
        request_body_data = {
            "payloadTemplate": payloadTemplate,
            "active": active,
            "subscriberUrl": subscriberUrl,
            "triggers": triggers,
            "secret": secret,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/webhooks"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createwebhookresponse.model_validate(self._handle_response(response))

    def get_organization_webhook_by_id(
        self, orgId: str, webhookId: str
    ) -> Createwebhookresponse:
        """
        Retrieves information about a specific webhook identified by `webhookId` for an organization specified by `orgId`.

        Args:
            orgId (string): orgId
            webhookId (string): webhookId

        Returns:
            Createwebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Webhooks
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/webhooks/{webhookId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Createwebhookresponse.model_validate(self._handle_response(response))

    def delete_organization_webhook_by_id(
        self, orgId: str, webhookId: str
    ) -> Createwebhookresponse:
        """
        Deletes a specified webhook from an organization using the provided organization and webhook identifiers.

        Args:
            orgId (string): orgId
            webhookId (string): webhookId

        Returns:
            Createwebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Webhooks
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        url = f"{self.base_url}/v2/organizations/{orgId}/webhooks/{webhookId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Createwebhookresponse.model_validate(self._handle_response(response))

    def update_webhook_by_id(
        self,
        orgId: str,
        webhookId: str,
        payloadTemplate: Optional[str] = None,
        active: Optional[bool] = None,
        subscriberUrl: Optional[str] = None,
        triggers: Optional[str] = None,
        secret: Optional[str] = None,
    ) -> Createwebhookresponse:
        """
        Updates a specific webhook for an organization using partial modifications via the PATCH method.

        Args:
            orgId (string): orgId
            webhookId (string): webhookId
            payloadTemplate (string): The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information Example: '{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}'.
            active (boolean): active
            subscriberUrl (string): subscriberUrl
            triggers (string): triggers Example: "['BOOKING_CREATED', 'BOOKING_RESCHEDULED', 'BOOKING_CANCELLED', 'BOOKING_CONFIRMED', 'BOOKING_REJECTED', 'BOOKING_COMPLETED', 'BOOKING_NO_SHOW', 'BOOKING_REOPENED']".
            secret (string): secret

        Returns:
            Createwebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Orgs / Webhooks
        """
        if orgId is None:
            raise ValueError("Missing required parameter 'orgId'.")
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        request_body_data = None
        request_body_data = {
            "payloadTemplate": payloadTemplate,
            "active": active,
            "subscriberUrl": subscriberUrl,
            "triggers": triggers,
            "secret": secret,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/organizations/{orgId}/webhooks/{webhookId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Createwebhookresponse.model_validate(self._handle_response(response))

    def list_bookings(
        self,
        status: Optional[List[str]] = None,
        attendeeEmail: Optional[str] = None,
        attendeeName: Optional[str] = None,
        eventTypeIds: Optional[str] = None,
        eventTypeId: Optional[str] = None,
        teamsIds: Optional[str] = None,
        teamId: Optional[str] = None,
        afterStart: Optional[str] = None,
        beforeEnd: Optional[str] = None,
        sortStart: Optional[str] = None,
        sortEnd: Optional[str] = None,
        sortCreated: Optional[str] = None,
        take: Optional[float] = None,
        skip: Optional[float] = None,
    ) -> Listbookingsresponse:
        """
        Retrieves a filtered list of bookings based on parameters like status, attendee details, event types, time ranges, and pagination settings.

        Args:
            status (array): Filter bookings by status. If you want to filter by multiple statuses, separate them with a comma. Example: '?status=upcoming,past'.
            attendeeEmail (string): Filter bookings by the attendee's email address. Example: 'example@domain.com'.
            attendeeName (string): Filter bookings by the attendee's name. Example: 'John Doe'.
            eventTypeIds (string): Filter bookings by event type ids belonging to the user. Event type ids must be separated by a comma. Example: '?eventTypeIds=100,200'.
            eventTypeId (string): Filter bookings by event type id belonging to the user. Example: '?eventTypeId=100'.
            teamsIds (string): Filter bookings by team ids that user is part of. Team ids must be separated by a comma. Example: '?teamIds=50,60'.
            teamId (string): Filter bookings by team id that user is part of Example: '?teamId=50'.
            afterStart (string): Filter bookings with start after this date string. Example: '?afterStart=2025-03-07T10:00:00.000Z'.
            beforeEnd (string): Filter bookings with end before this date string. Example: '?beforeEnd=2025-03-07T11:00:00.000Z'.
            sortStart (string): Sort results by their start time in ascending or descending order. Example: '?sortStart=asc OR ?sortStart=desc'.
            sortEnd (string): Sort results by their end time in ascending or descending order. Example: '?sortEnd=asc OR ?sortEnd=desc'.
            sortCreated (string): Sort results by their creation time (when booking was made) in ascending or descending order. Example: '?sortCreated=asc OR ?sortCreated=desc'.
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Listbookingsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Bookings
        """
        url = f"{self.base_url}/v2/bookings"
        query_params = {
            k: v
            for k, v in [
                ("status", status),
                ("attendeeEmail", attendeeEmail),
                ("attendeeName", attendeeName),
                ("eventTypeIds", eventTypeIds),
                ("eventTypeId", eventTypeId),
                ("teamsIds", teamsIds),
                ("teamId", teamId),
                ("afterStart", afterStart),
                ("beforeEnd", beforeEnd),
                ("sortStart", sortStart),
                ("sortEnd", sortEnd),
                ("sortCreated", sortCreated),
                ("take", take),
                ("skip", skip),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Listbookingsresponse.model_validate(self._handle_response(response))

    def get_booking_by_uid(self, bookingUid: str) -> Getbookingbyuidresponse:
        """
        Retrieves the details of a specific booking using its unique identifier.

        Args:
            bookingUid (string): bookingUid

        Returns:
            Getbookingbyuidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Bookings
        """
        if bookingUid is None:
            raise ValueError("Missing required parameter 'bookingUid'.")
        url = f"{self.base_url}/v2/bookings/{bookingUid}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getbookingbyuidresponse.model_validate(self._handle_response(response))

    def reschedule_booking_by_uid(
        self, bookingUid: str
    ) -> Reschedulebookingbyuidresponse:
        """
        Reschedules an existing booking identified by its unique `bookingUid`, using the `POST` method at the "/v2/bookings/{bookingUid}/reschedule" endpoint.

        Args:
            bookingUid (string): bookingUid

        Returns:
            Reschedulebookingbyuidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Bookings
        """
        if bookingUid is None:
            raise ValueError("Missing required parameter 'bookingUid'.")
        request_body_data = None
        url = f"{self.base_url}/v2/bookings/{bookingUid}/reschedule"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Reschedulebookingbyuidresponse.model_validate(
            self._handle_response(response)
        )

    def cancel_booking_by_uid(self, bookingUid: str) -> Cancelbookingbyuidresponse:
        """
        Cancels a booking by sending a POST request to the "/v2/bookings/{bookingUid}/cancel" endpoint, using the provided booking UID to identify the booking to be canceled.

        Args:
            bookingUid (string): bookingUid

        Returns:
            Cancelbookingbyuidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Bookings
        """
        if bookingUid is None:
            raise ValueError("Missing required parameter 'bookingUid'.")
        request_body_data = None
        url = f"{self.base_url}/v2/bookings/{bookingUid}/cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Cancelbookingbyuidresponse.model_validate(
            self._handle_response(response)
        )

    def mark_booking_absent_by_uid(
        self,
        bookingUid: str,
        host: Optional[bool] = None,
        attendees: Optional[List[dict[str, Any]]] = None,
    ) -> Markbookingabsentbyuidresponse:
        """
        Marks a booking as absent using the provided booking UID and authentication token, indicating that the owner of the booking is absent.

        Args:
            bookingUid (string): bookingUid
            host (boolean): Whether the host was absent Example: 'False'.
            attendees (array): attendees

        Returns:
            Markbookingabsentbyuidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Bookings
        """
        if bookingUid is None:
            raise ValueError("Missing required parameter 'bookingUid'.")
        request_body_data = None
        request_body_data = {
            "host": host,
            "attendees": attendees,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/bookings/{bookingUid}/mark-absent"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Markbookingabsentbyuidresponse.model_validate(
            self._handle_response(response)
        )

    def reassign_booking(self, bookingUid: str) -> Reassignbookingresponse:
        """
        Reassigns a booking to a different team member or booking page via a POST request to the specified booking UID, potentially allowing double bookings if availability conflicts exist.

        Args:
            bookingUid (string): bookingUid

        Returns:
            Reassignbookingresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Bookings
        """
        if bookingUid is None:
            raise ValueError("Missing required parameter 'bookingUid'.")
        request_body_data = None
        url = f"{self.base_url}/v2/bookings/{bookingUid}/reassign"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Reassignbookingresponse.model_validate(self._handle_response(response))

    def reassign_booking_to_user(
        self, bookingUid: str, userId: str, reason: Optional[str] = None
    ) -> Reassignbookingresponse:
        """
        Reassigns a booking to a specific user specified by the `userId` using a POST request, requiring authorization and providing a reason for the reassignment.

        Args:
            bookingUid (string): bookingUid
            userId (string): userId
            reason (string): Reason for reassigning the booking Example: 'Host has to take another call'.

        Returns:
            Reassignbookingresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Bookings
        """
        if bookingUid is None:
            raise ValueError("Missing required parameter 'bookingUid'.")
        if userId is None:
            raise ValueError("Missing required parameter 'userId'.")
        request_body_data = None
        request_body_data = {
            "reason": reason,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/bookings/{bookingUid}/reassign/{userId}"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Reassignbookingresponse.model_validate(self._handle_response(response))

    def confirm_booking(self, bookingUid: str) -> Getbookingbyuidresponse:
        """
        Confirms a specific booking by its unique identifier and returns a success status upon completion.

        Args:
            bookingUid (string): bookingUid

        Returns:
            Getbookingbyuidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Bookings
        """
        if bookingUid is None:
            raise ValueError("Missing required parameter 'bookingUid'.")
        request_body_data = None
        url = f"{self.base_url}/v2/bookings/{bookingUid}/confirm"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Getbookingbyuidresponse.model_validate(self._handle_response(response))

    def decline_booking(
        self, bookingUid: str, reason: Optional[str] = None
    ) -> Getbookingbyuidresponse:
        """
        Declines a specific booking identified by the bookingUid using the Booking.com API and returns a success status upon completion.

        Args:
            bookingUid (string): bookingUid
            reason (string): Reason for declining a booking that requires a confirmation Example: 'Host has to take another call'.

        Returns:
            Getbookingbyuidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Bookings
        """
        if bookingUid is None:
            raise ValueError("Missing required parameter 'bookingUid'.")
        request_body_data = None
        request_body_data = {
            "reason": reason,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/bookings/{bookingUid}/decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Getbookingbyuidresponse.model_validate(self._handle_response(response))

    def save_ics_feed_post(
        self, urls: List[str], readOnly: Optional[bool] = None
    ) -> Saveicsfeedpostresponse:
        """
        Saves an ICS calendar feed configuration and returns the created resource.

        Args:
            urls (array): An array of ICS URLs Example: "['https://cal.com/ics/feed.ics', 'http://cal.com/ics/feed.ics']".
            readOnly (boolean): Whether to allowing writing to the calendar or not Example: 'False'.

        Returns:
            Saveicsfeedpostresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Calendars
        """
        request_body_data = None
        request_body_data = {
            "urls": urls,
            "readOnly": readOnly,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/calendars/ics-feed/save"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Saveicsfeedpostresponse.model_validate(self._handle_response(response))

    def check_ics_feed(self) -> Checkicsfeedresponse:
        """
        Checks the status and validity of an ICS calendar feed.

        Returns:
            Checkicsfeedresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Calendars
        """
        url = f"{self.base_url}/v2/calendars/ics-feed/check"
        query_params = {}
        response = self._get(url, params=query_params)
        return Checkicsfeedresponse.model_validate(self._handle_response(response))

    def get_calendars_busy_times(
        self,
        loggedInUsersTz: str,
        credentialId: float,
        externalId: str,
        dateFrom: Optional[str] = None,
        dateTo: Optional[str] = None,
    ) -> Getcalendarsbusytimesresponse:
        """
        Retrieves a list of busy times for specified calendars within a given date range using the "GET" method at "/v2/calendars/busy-times," allowing for time zone and credential specification.

        Args:
            loggedInUsersTz (string): The timezone of the logged in user represented as a string Example: 'America/New_York'.
            credentialId (number): A unique identifier for the credential associated with the request, used to authenticate or authorize access when retrieving busy times for calendars.
            externalId (string): The `externalId` query parameter uniquely identifies a user or resource in an external system to retrieve their busy calendar times.
            dateFrom (string): The starting date for the busy times query Example: '2023-10-01'.
            dateTo (string): The ending date for the busy times query Example: '2023-10-31'.

        Returns:
            Getcalendarsbusytimesresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Calendars
        """
        url = f"{self.base_url}/v2/calendars/busy-times"
        query_params = {
            k: v
            for k, v in [
                ("loggedInUsersTz", loggedInUsersTz),
                ("dateFrom", dateFrom),
                ("dateTo", dateTo),
                ("credentialId", credentialId),
                ("externalId", externalId),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Getcalendarsbusytimesresponse.model_validate(
            self._handle_response(response)
        )

    def get_calendars(self) -> Getcalendarsresponse:
        """
        Retrieves a list of calendars using the API at the "/v2/calendars" endpoint via the GET method.

        Returns:
            Getcalendarsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Calendars
        """
        url = f"{self.base_url}/v2/calendars"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getcalendarsresponse.model_validate(self._handle_response(response))

    def calendars_controller_redirect(self, calendar: str) -> Checkicsfeedresponse:
        """
        Retrieves a connection status for the specified calendar at path "/v2/calendars/{calendar}/connect" using the GET method, requiring authorization and calendar identifier.

        Args:
            calendar (string): calendar

        Returns:
            Checkicsfeedresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Calendars
        """
        if calendar is None:
            raise ValueError("Missing required parameter 'calendar'.")
        url = f"{self.base_url}/v2/calendars/{calendar}/connect"
        query_params = {}
        response = self._get(url, params=query_params)
        return Checkicsfeedresponse.model_validate(self._handle_response(response))

    def calendars_controller_save(self, calendar: str, state: str, code: str) -> Any:
        """
        Retrieves the saved state of a specified calendar using the given parameters.

        Args:
            calendar (string): calendar
            state (string): Optional query parameter to specify additional context or application state for the calendar save operation.
            code (string): Optional code query parameter used to specify additional context or identifier for saving a calendar.

        Returns:
            Any: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Calendars
        """
        if calendar is None:
            raise ValueError("Missing required parameter 'calendar'.")
        url = f"{self.base_url}/v2/calendars/{calendar}/save"
        query_params = {
            k: v for k, v in [("state", state), ("code", code)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_calendar_credentials(self, calendar: str) -> Any:
        """
        Creates credentials for a specified Google Calendar using the POST method at the "/v2/calendars/{calendar}/credentials" path.

        Args:
            calendar (string): calendar

        Returns:
            Any: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Calendars
        """
        if calendar is None:
            raise ValueError("Missing required parameter 'calendar'.")
        request_body_data = None
        url = f"{self.base_url}/v2/calendars/{calendar}/credentials"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def calendars_controller_check(self, calendar: str) -> Checkicsfeedresponse:
        """
        Checks the status or availability of a specified calendar using the "GET" method at the "/v2/calendars/{calendar}/check" endpoint.

        Args:
            calendar (string): calendar

        Returns:
            Checkicsfeedresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Calendars
        """
        if calendar is None:
            raise ValueError("Missing required parameter 'calendar'.")
        url = f"{self.base_url}/v2/calendars/{calendar}/check"
        query_params = {}
        response = self._get(url, params=query_params)
        return Checkicsfeedresponse.model_validate(self._handle_response(response))

    def disconnect_calendar(self, calendar: str, id: int) -> Disconnectcalendarresponse:
        """
        Disconnects a specified calendar from a user's account using the Cal.com API, requiring a POST request to the "/v2/calendars/{calendar}/disconnect" endpoint with the calendar type and credential ID in the request body.

        Args:
            calendar (string): calendar
            id (integer): Credential ID of the calendar to delete, as returned by the /calendars endpoint Example: '10'.

        Returns:
            Disconnectcalendarresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Calendars
        """
        if calendar is None:
            raise ValueError("Missing required parameter 'calendar'.")
        request_body_data = None
        request_body_data = {
            "id": id,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/calendars/{calendar}/disconnect"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Disconnectcalendarresponse.model_validate(
            self._handle_response(response)
        )

    def conferencing_controller_connect(
        self, app: str
    ) -> ConferencingcontrollerConnectresponse:
        """
        Establishes a connection for conferencing using the specified application via the POST method at the "/v2/conferencing/{app}/connect" endpoint.

        Args:
            app (string): app

        Returns:
            ConferencingcontrollerConnectresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Conferencing
        """
        if app is None:
            raise ValueError("Missing required parameter 'app'.")
        request_body_data = None
        url = f"{self.base_url}/v2/conferencing/{app}/connect"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return ConferencingcontrollerConnectresponse.model_validate(
            self._handle_response(response)
        )

    def get_auth_url(
        self, app: str, returnTo: str, onErrorReturnTo: str
    ) -> Getprovideraccesstokenresponse:
        """
        Generates an authorization URL for OAuth in a conferencing application using the "GET" method at the "/v2/conferencing/{app}/oauth/auth-url" path, accepting parameters such as the application name and return URLs.

        Args:
            app (string): app
            returnTo (string): Specifies the URL to redirect to after the OAuth authentication process completes.
            onErrorReturnTo (string): URL to redirect to when an error occurs during the authorization flow, allowing for error handling and fallback behavior.

        Returns:
            Getprovideraccesstokenresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Conferencing
        """
        if app is None:
            raise ValueError("Missing required parameter 'app'.")
        url = f"{self.base_url}/v2/conferencing/{app}/oauth/auth-url"
        query_params = {
            k: v
            for k, v in [("returnTo", returnTo), ("onErrorReturnTo", onErrorReturnTo)]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Getprovideraccesstokenresponse.model_validate(
            self._handle_response(response)
        )

    def conferencing_controller_save(self, app: str, state: str, code: str) -> Any:
        """
        Handles OAuth authorization callbacks for conferencing applications, processing authorization codes and states to authenticate users via the "GET" method.

        Args:
            app (string): app
            state (string): A CSRF protection token passed between authorization request and callback, used to verify request authenticity and optionally maintain application state.
            code (string): Authorization code returned from the OAuth provider after user authentication.

        Returns:
            Any: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Conferencing
        """
        if app is None:
            raise ValueError("Missing required parameter 'app'.")
        url = f"{self.base_url}/v2/conferencing/{app}/oauth/callback"
        query_params = {
            k: v for k, v in [("state", state), ("code", code)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_conferencing(self) -> Listconferencingresponse:
        """
        Retrieves conferencing data using the "GET" method at the "/v2/conferencing" endpoint, returning relevant information.

        Returns:
            Listconferencingresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Conferencing
        """
        url = f"{self.base_url}/v2/conferencing"
        query_params = {}
        response = self._get(url, params=query_params)
        return Listconferencingresponse.model_validate(self._handle_response(response))

    def conferencing_controller_default(
        self, app: str
    ) -> Getprovideraccesstokenresponse:
        """
        Sets the default conferencing application for the specified app identifier.

        Args:
            app (string): app

        Returns:
            Getprovideraccesstokenresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Conferencing
        """
        if app is None:
            raise ValueError("Missing required parameter 'app'.")
        request_body_data = None
        url = f"{self.base_url}/v2/conferencing/{app}/default"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Getprovideraccesstokenresponse.model_validate(
            self._handle_response(response)
        )

    def get_default_conferencing(self) -> Getdefaultconferencingresponse:
        """
        Retrieves the default conferencing configuration from the API.

        Returns:
            Getdefaultconferencingresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Conferencing
        """
        url = f"{self.base_url}/v2/conferencing/default"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getdefaultconferencingresponse.model_validate(
            self._handle_response(response)
        )

    def disconnect_conferencing_app(self, app: str) -> Getprovideraccesstokenresponse:
        """
        Disconnects all participants from a specified conferencing application instance using the path parameter and returns a success response upon completion.

        Args:
            app (string): app

        Returns:
            Getprovideraccesstokenresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Conferencing
        """
        if app is None:
            raise ValueError("Missing required parameter 'app'.")
        url = f"{self.base_url}/v2/conferencing/{app}/disconnect"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Getprovideraccesstokenresponse.model_validate(
            self._handle_response(response)
        )

    def update_destination_calendars(
        self, integration: str, externalId: str
    ) -> Updatedestinationcalendarsresponse:
        """
        Updates a destination calendar at the specified path "/v2/destination-calendars" using the PUT method.

        Args:
            integration (string): The calendar service you want to integrate, as returned by the /calendars endpoint Example: 'apple_calendar'.
            externalId (string): Unique identifier used to represent the specfic calendar, as returned by the /calendars endpoint Example: 'https://caldav.icloud.com/26962146906/calendars/1644422A-1945-4438-BBC0-4F0Q23A57R7S/'.

        Returns:
            Updatedestinationcalendarsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Destination Calendars
        """
        request_body_data = None
        request_body_data = {
            "integration": integration,
            "externalId": externalId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/destination-calendars"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Updatedestinationcalendarsresponse.model_validate(
            self._handle_response(response)
        )

    def list_event_types(
        self,
        username: Optional[str] = None,
        eventSlug: Optional[str] = None,
        usernames: Optional[str] = None,
        orgSlug: Optional[str] = None,
        orgId: Optional[float] = None,
    ) -> Listeventtypesresponse:
        """
        Retrieves a list of event types using the GET method, allowing filtering by username, event slug, usernames list, organization slug, and organization ID through query parameters.

        Args:
            username (string): The username of the user to get event types for. If only username provided will get all event types.
            eventSlug (string): Slug of event type to return. Notably, if eventSlug is provided then username must be provided too, because multiple users can have event with same slug.
            usernames (string): Get dynamic event type for multiple usernames separated by comma. e.g `usernames=alice,bob`
            orgSlug (string): slug of the user's organization if he is in one, orgId is not required if using this parameter
            orgId (number): ID of the organization of the user you want the get the event-types of, orgSlug is not needed when using this parameter

        Returns:
            Listeventtypesresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Event Types
        """
        url = f"{self.base_url}/v2/event-types"
        query_params = {
            k: v
            for k, v in [
                ("username", username),
                ("eventSlug", eventSlug),
                ("usernames", usernames),
                ("orgSlug", orgSlug),
                ("orgId", orgId),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Listeventtypesresponse.model_validate(self._handle_response(response))

    def get_event_type_by_id(self, eventTypeId: str) -> Geteventtypebyidresponse:
        """
        Retrieves detailed information about a specific event type by its ID using the Events API.

        Args:
            eventTypeId (string): eventTypeId

        Returns:
            Geteventtypebyidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Event Types
        """
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        url = f"{self.base_url}/v2/event-types/{eventTypeId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Geteventtypebyidresponse.model_validate(self._handle_response(response))

    def delete_event_type_by_id(self, eventTypeId: str) -> Deleteeventtypebyidresponse:
        """
        Deletes the specified event type using the provided ID and returns a success status upon completion.

        Args:
            eventTypeId (string): eventTypeId

        Returns:
            Deleteeventtypebyidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Event Types
        """
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        url = f"{self.base_url}/v2/event-types/{eventTypeId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Deleteeventtypebyidresponse.model_validate(
            self._handle_response(response)
        )

    def create_event_type_webhook(
        self,
        eventTypeId: str,
        active: bool,
        subscriberUrl: str,
        triggers: str,
        payloadTemplate: Optional[str] = None,
        secret: Optional[str] = None,
    ) -> Createeventtypewebhookresponse:
        """
        Creates a webhook subscription for a specific event type, returning a success status upon creation.

        Args:
            eventTypeId (string): eventTypeId
            active (boolean): active
            subscriberUrl (string): subscriberUrl
            triggers (string): triggers Example: "['BOOKING_CREATED', 'BOOKING_RESCHEDULED', 'BOOKING_CANCELLED', 'BOOKING_CONFIRMED', 'BOOKING_REJECTED', 'BOOKING_COMPLETED', 'BOOKING_NO_SHOW', 'BOOKING_REOPENED']".
            payloadTemplate (string): The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information Example: '{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}'.
            secret (string): secret

        Returns:
            Createeventtypewebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Event Types / Webhooks
        """
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        request_body_data = None
        request_body_data = {
            "payloadTemplate": payloadTemplate,
            "active": active,
            "subscriberUrl": subscriberUrl,
            "triggers": triggers,
            "secret": secret,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/event-types/{eventTypeId}/webhooks"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createeventtypewebhookresponse.model_validate(
            self._handle_response(response)
        )

    def get_event_webhooks(
        self,
        eventTypeId: str,
        take: Optional[float] = None,
        skip: Optional[float] = None,
    ) -> Geteventwebhooksresponse:
        """
        Retrieves a list of webhooks configured for a specific event type, supporting pagination via take and skip parameters.

        Args:
            eventTypeId (string): eventTypeId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Geteventwebhooksresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Event Types / Webhooks
        """
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        url = f"{self.base_url}/v2/event-types/{eventTypeId}/webhooks"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Geteventwebhooksresponse.model_validate(self._handle_response(response))

    def delete_event_webhook(self, eventTypeId: str) -> Deleteclientwebhookresponse:
        """
        Deletes a webhook associated with a specific event type ID using the DELETE method.

        Args:
            eventTypeId (string): eventTypeId

        Returns:
            Deleteclientwebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Event Types / Webhooks
        """
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        url = f"{self.base_url}/v2/event-types/{eventTypeId}/webhooks"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Deleteclientwebhookresponse.model_validate(
            self._handle_response(response)
        )

    def patch_event_type_webhook_by_id(
        self,
        eventTypeId: str,
        webhookId: str,
        payloadTemplate: Optional[str] = None,
        active: Optional[bool] = None,
        subscriberUrl: Optional[str] = None,
        triggers: Optional[str] = None,
        secret: Optional[str] = None,
    ) -> Createeventtypewebhookresponse:
        """
        Updates a webhook associated with a specific event type using the PATCH method, modifying its properties at the path "/v2/event-types/{eventTypeId}/webhooks/{webhookId}".

        Args:
            eventTypeId (string): eventTypeId
            webhookId (string): webhookId
            payloadTemplate (string): The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information Example: '{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}'.
            active (boolean): active
            subscriberUrl (string): subscriberUrl
            triggers (string): triggers Example: "['BOOKING_CREATED', 'BOOKING_RESCHEDULED', 'BOOKING_CANCELLED', 'BOOKING_CONFIRMED', 'BOOKING_REJECTED', 'BOOKING_COMPLETED', 'BOOKING_NO_SHOW', 'BOOKING_REOPENED']".
            secret (string): secret

        Returns:
            Createeventtypewebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Event Types / Webhooks
        """
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        request_body_data = None
        request_body_data = {
            "payloadTemplate": payloadTemplate,
            "active": active,
            "subscriberUrl": subscriberUrl,
            "triggers": triggers,
            "secret": secret,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/event-types/{eventTypeId}/webhooks/{webhookId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Createeventtypewebhookresponse.model_validate(
            self._handle_response(response)
        )

    def get_webhook_by_id(
        self, eventTypeId: str, webhookId: str
    ) -> Createeventtypewebhookresponse:
        """
        Retrieves details about a specific webhook for a given event type using the provided event type ID and webhook ID.

        Args:
            eventTypeId (string): eventTypeId
            webhookId (string): webhookId

        Returns:
            Createeventtypewebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Event Types / Webhooks
        """
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        url = f"{self.base_url}/v2/event-types/{eventTypeId}/webhooks/{webhookId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Createeventtypewebhookresponse.model_validate(
            self._handle_response(response)
        )

    def delete_event_type_webhook_by_id(
        self, eventTypeId: str, webhookId: str
    ) -> Createeventtypewebhookresponse:
        """
        Deletes a webhook associated with a specific event type using the provided `eventTypeId` and `webhookId` parameters.

        Args:
            eventTypeId (string): eventTypeId
            webhookId (string): webhookId

        Returns:
            Createeventtypewebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Event Types / Webhooks
        """
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        url = f"{self.base_url}/v2/event-types/{eventTypeId}/webhooks/{webhookId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Createeventtypewebhookresponse.model_validate(
            self._handle_response(response)
        )

    def me_controller_get_me(self) -> MecontrollerGetmeresponse:
        """
        Retrieves the authenticated user's profile information and returns it in the API response.

        Returns:
            MecontrollerGetmeresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Me
        """
        url = f"{self.base_url}/v2/me"
        query_params = {}
        response = self._get(url, params=query_params)
        return MecontrollerGetmeresponse.model_validate(self._handle_response(response))

    def me_controller_update_me(
        self,
        email: Optional[str] = None,
        name: Optional[str] = None,
        timeFormat: Optional[float] = None,
        defaultScheduleId: Optional[float] = None,
        weekStart: Optional[str] = None,
        timeZone: Optional[str] = None,
        locale: Optional[str] = None,
        avatarUrl: Optional[str] = None,
    ) -> MecontrollerGetmeresponse:
        """
        Updates the properties of the current user's profile at the "/v2/me" path using the PATCH method.

        Args:
            email (string): email
            name (string): name
            timeFormat (number): Must be 12 or 24 Example: '12'.
            defaultScheduleId (number): defaultScheduleId
            weekStart (string): weekStart Example: 'Monday'.
            timeZone (string): timeZone
            locale (string): locale Example: 'en'.
            avatarUrl (string): URL of the user's avatar image Example: 'https://cal.com/api/avatar/2b735186-b01b-46d3-87da-019b8f61776b.png'.

        Returns:
            MecontrollerGetmeresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Me
        """
        request_body_data = None
        request_body_data = {
            "email": email,
            "name": name,
            "timeFormat": timeFormat,
            "defaultScheduleId": defaultScheduleId,
            "weekStart": weekStart,
            "timeZone": timeZone,
            "locale": locale,
            "avatarUrl": avatarUrl,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/me"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return MecontrollerGetmeresponse.model_validate(self._handle_response(response))

    def create_schedule(
        self,
        name: str,
        timeZone: str,
        isDefault: bool,
        availability: Optional[List[dict[str, Any]]] = None,
        overrides: Optional[List[dict[str, Any]]] = None,
    ) -> Createuserscheduleresponse:
        """
        Creates a new schedule using the provided data and returns a successful creation response with a 201 status code.

        Args:
            name (string): name Example: 'Catch up hours'.
            timeZone (string): Timezone is used to calculate available times when an event using the schedule is booked. Example: 'Europe/Rome'.
            isDefault (boolean): Each user should have 1 default schedule. If you specified `timeZone` when creating managed user, then the default schedule will be created with that timezone.
            Default schedule means that if an event type is not tied to a specific schedule then the default schedule is used. Example: 'True'.
            availability (array): Each object contains days and times when the user is available. If not passed, the default availability is Monday to Friday from 09:00 to 17:00. Example: "[{'days': ['Monday', 'Tuesday'], 'startTime': '17:00', 'endTime': '19:00'}, {'days': ['Wednesday', 'Thursday'], 'startTime': '16:00', 'endTime': '20:00'}]".
            overrides (array): Need to change availability for a specific date? Add an override. Example: "[{'date': '2024-05-20', 'startTime': '18:00', 'endTime': '21:00'}]".

        Returns:
            Createuserscheduleresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Schedules
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "timeZone": timeZone,
            "availability": availability,
            "isDefault": isDefault,
            "overrides": overrides,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/schedules"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createuserscheduleresponse.model_validate(
            self._handle_response(response)
        )

    def list_schedules(self) -> Getorganizationschedulesresponse:
        """
        Retrieves a list of schedules using specified authorization headers and API version.

        Returns:
            Getorganizationschedulesresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Schedules
        """
        url = f"{self.base_url}/v2/schedules"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getorganizationschedulesresponse.model_validate(
            self._handle_response(response)
        )

    def get_default_schedule(self) -> Createuserscheduleresponse:
        """
        Retrieves the default schedule of the authenticated user using the Cal.com API, returning relevant scheduling information.

        Returns:
            Createuserscheduleresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Schedules
        """
        url = f"{self.base_url}/v2/schedules/default"
        query_params = {}
        response = self._get(url, params=query_params)
        return Createuserscheduleresponse.model_validate(
            self._handle_response(response)
        )

    def get_schedule_by_id(self, scheduleId: str) -> Getscheduledetailresponse:
        """
        Retrieves a specific schedule by its ID using the "GET" method at the "/v2/schedules/{scheduleId}" endpoint.

        Args:
            scheduleId (string): scheduleId

        Returns:
            Getscheduledetailresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Schedules
        """
        if scheduleId is None:
            raise ValueError("Missing required parameter 'scheduleId'.")
        url = f"{self.base_url}/v2/schedules/{scheduleId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getscheduledetailresponse.model_validate(self._handle_response(response))

    def update_schedule_by_id(
        self,
        scheduleId: str,
        name: Optional[str] = None,
        timeZone: Optional[str] = None,
        availability: Optional[List[dict[str, Any]]] = None,
        isDefault: Optional[bool] = None,
        overrides: Optional[List[dict[str, Any]]] = None,
    ) -> Updateuserschedulebyidresponse:
        """
        Updates a schedule's configuration partially by specifying scheduleId and modified fields in the request body, returning a success status upon completion.

        Args:
            scheduleId (string): scheduleId
            name (string): name Example: 'One-on-one coaching'.
            timeZone (string): timeZone Example: 'Europe/Rome'.
            availability (array): availability Example: "[{'days': ['Monday', 'Tuesday'], 'startTime': '09:00', 'endTime': '10:00'}]".
            isDefault (boolean): isDefault Example: 'True'.
            overrides (array): overrides Example: "[{'date': '2024-05-20', 'startTime': '12:00', 'endTime': '14:00'}]".

        Returns:
            Updateuserschedulebyidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Schedules
        """
        if scheduleId is None:
            raise ValueError("Missing required parameter 'scheduleId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "timeZone": timeZone,
            "availability": availability,
            "isDefault": isDefault,
            "overrides": overrides,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/schedules/{scheduleId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Updateuserschedulebyidresponse.model_validate(
            self._handle_response(response)
        )

    def delete_schedule_by_id(self, scheduleId: str) -> Getprovideraccesstokenresponse:
        """
        Deletes a specific schedule identified by the `scheduleId` using the `DELETE` method.

        Args:
            scheduleId (string): scheduleId

        Returns:
            Getprovideraccesstokenresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Schedules
        """
        if scheduleId is None:
            raise ValueError("Missing required parameter 'scheduleId'.")
        url = f"{self.base_url}/v2/schedules/{scheduleId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Getprovideraccesstokenresponse.model_validate(
            self._handle_response(response)
        )

    def add_selected_calendar(
        self, integration: str, externalId: str, credentialId: float
    ) -> Updatedestinationcalendarsresponse:
        """
        Creates a new selected calendar entry for external integrations using provided identifiers.

        Args:
            integration (string): integration
            externalId (string): externalId
            credentialId (number): credentialId

        Returns:
            Updatedestinationcalendarsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Selected Calendars
        """
        request_body_data = None
        request_body_data = {
            "integration": integration,
            "externalId": externalId,
            "credentialId": credentialId,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/selected-calendars"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Updatedestinationcalendarsresponse.model_validate(
            self._handle_response(response)
        )

    def delete_selected_calendars(
        self, integration: str, externalId: str, credentialId: str
    ) -> Updatedestinationcalendarsresponse:
        """
        Deletes one or more selected calendars based on integration, external ID, and credential ID using the DELETE method at the "/v2/selected-calendars" path.

        Args:
            integration (string): Specifies the calendar integration platform to remove from the selected calendars.
            externalId (string): The "externalId" query parameter is used during the DELETE operation to specify the unique identifier of the selected calendar to be removed.
            credentialId (string): The credentialId in the query specifies the unique identifier of the credential to be deleted for the selected calendar.

        Returns:
            Updatedestinationcalendarsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Selected Calendars
        """
        url = f"{self.base_url}/v2/selected-calendars"
        query_params = {
            k: v
            for k, v in [
                ("integration", integration),
                ("externalId", externalId),
                ("credentialId", credentialId),
            ]
            if v is not None
        }
        response = self._delete(url, params=query_params)
        return Updatedestinationcalendarsresponse.model_validate(
            self._handle_response(response)
        )

    def slots_controller_reserve_slot(
        self,
        eventTypeId: float,
        slotUtcStartDate: str,
        slotUtcEndDate: str,
        bookingUid: Optional[str] = None,
    ) -> SlotscontrollerReserveslotresponse:
        """
        Reserves a slot using the "POST" method at "/v2/slots/reserve", creating a new reservation and returning a successful response when the operation is completed.

        Args:
            eventTypeId (number): Event Type ID for which timeslot is being reserved. Example: '100'.
            slotUtcStartDate (string): Start date of the slot in UTC timezone. Example: '2022-06-14T00:00:00.000Z'.
            slotUtcEndDate (string): End date of the slot in UTC timezone. Example: '2022-06-14T00:30:00.000Z'.
            bookingUid (string): Optional but only for events with seats. Used to retrieve booking of a seated event.

        Returns:
            SlotscontrollerReserveslotresponse: Successful response returning uid of reserved slot.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Slots
        """
        request_body_data = None
        request_body_data = {
            "eventTypeId": eventTypeId,
            "slotUtcStartDate": slotUtcStartDate,
            "slotUtcEndDate": slotUtcEndDate,
            "bookingUid": bookingUid,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/slots/reserve"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return SlotscontrollerReserveslotresponse.model_validate(
            self._handle_response(response)
        )

    def delete_selected_slot(self, uid: str) -> Deleteselectedslotresponse:
        """
        Deletes the specified slot identified by the uid parameter and returns a successful response upon completion.

        Args:
            uid (string): Unique identifier for the slot to be removed. Example: 'e2a7bcf9-cc7b-40a0-80d3-657d391775a6'.

        Returns:
            Deleteselectedslotresponse: Response deleting reserved slot by uid.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Slots
        """
        url = f"{self.base_url}/v2/slots/selected-slot"
        query_params = {k: v for k, v in [("uid", uid)] if v is not None}
        response = self._delete(url, params=query_params)
        return Deleteselectedslotresponse.model_validate(
            self._handle_response(response)
        )

    def list_available_slots(
        self,
        startTime: str,
        endTime: str,
        eventTypeId: float,
        eventTypeSlug: Optional[str] = None,
        usernameList: Optional[List[str]] = None,
        duration: Optional[float] = None,
        rescheduleUid: Optional[str] = None,
        timeZone: Optional[str] = None,
        orgSlug: Optional[str] = None,
        slotFormat: Optional[str] = None,
    ) -> Listavailableslotsresponse:
        """
        Retrieves a list of available slots within a specified time range, filtered by event type, user list, and other criteria, using the `GET` method at `/v2/slots/available`.

        Args:
            startTime (string): Start date string starting from which to fetch slots in UTC timezone. Example: '2022-06-14T00:00:00.000Z'.
            endTime (string): End date string until which to fetch slots in UTC timezone. Example: '2022-06-14T23:59:59.999Z'.
            eventTypeId (number): Event Type ID for which slots are being fetched. Example: '100'.
            eventTypeSlug (string): Slug of the event type for which slots are being fetched.
            usernameList (array): Only for dynamic events - list of usernames for which slots are being fetched.
            duration (number): Only for dynamic events - length of returned slots.
            rescheduleUid (string): Unique identifier used for rescheduling purposes, passed as a query parameter to filter available slots.
            timeZone (string): Specifies the time zone for available slots to be returned, using IANA time zone database names (e.g., "America/New_York").
            orgSlug (string): Organization slug.
            slotFormat (string): Format of slot times in response. Use 'range' to get start and end times. Example: 'range'.

        Returns:
            Listavailableslotsresponse: Available time slots retrieved successfully

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Slots
        """
        url = f"{self.base_url}/v2/slots/available"
        query_params = {
            k: v
            for k, v in [
                ("startTime", startTime),
                ("endTime", endTime),
                ("eventTypeId", eventTypeId),
                ("eventTypeSlug", eventTypeSlug),
                ("usernameList", usernameList),
                ("duration", duration),
                ("rescheduleUid", rescheduleUid),
                ("timeZone", timeZone),
                ("orgSlug", orgSlug),
                ("slotFormat", slotFormat),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return Listavailableslotsresponse.model_validate(
            self._handle_response(response)
        )

    def stripe_controller_redirect(self) -> GcalcontrollerRedirectresponse:
        """
        Retrieves details of a connected Stripe account using the Stripe-Account header for authorization.

        Returns:
            GcalcontrollerRedirectresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Stripe
        """
        url = f"{self.base_url}/v2/stripe/connect"
        query_params = {}
        response = self._get(url, params=query_params)
        return GcalcontrollerRedirectresponse.model_validate(
            self._handle_response(response)
        )

    def stripe_controller_save(
        self, state: str, code: str
    ) -> GcalcontrollerSaveresponse:
        """
        Retrieves a Stripe resource using a state and code query parameter and returns the result upon successful authentication.

        Args:
            state (string): A string value used to prevent cross-site request forgery (CSRF) attacks, returned unmodified in responses.
            code (string): The authorization code used to authenticate or authorize the request.

        Returns:
            GcalcontrollerSaveresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Stripe
        """
        url = f"{self.base_url}/v2/stripe/save"
        query_params = {
            k: v for k, v in [("state", state), ("code", code)] if v is not None
        }
        response = self._get(url, params=query_params)
        return GcalcontrollerSaveresponse.model_validate(
            self._handle_response(response)
        )

    def stripe_controller_check(self) -> StripecontrollerCheckresponse:
        """
        Checks system status or configuration in Stripe's v2 API and returns a success response.

        Returns:
            StripecontrollerCheckresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Stripe
        """
        url = f"{self.base_url}/v2/stripe/check"
        query_params = {}
        response = self._get(url, params=query_params)
        return StripecontrollerCheckresponse.model_validate(
            self._handle_response(response)
        )

    def get_team_stripe_check(self, teamId: str) -> StripecontrollerCheckresponse:
        """
        Retrieves Stripe payment or subscription data for a specific team using the provided `teamId` and returns relevant information via a GET request.

        Args:
            teamId (string): teamId

        Returns:
            StripecontrollerCheckresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Stripe
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        url = f"{self.base_url}/v2/stripe/check/{teamId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return StripecontrollerCheckresponse.model_validate(
            self._handle_response(response)
        )

    def teams_controller_create_team(
        self,
        name: str,
        slug: Optional[str] = None,
        logoUrl: Optional[str] = None,
        calVideoLogo: Optional[str] = None,
        appLogo: Optional[str] = None,
        appIconLogo: Optional[str] = None,
        bio: Optional[str] = None,
        hideBranding: Optional[bool] = None,
        isPrivate: Optional[bool] = None,
        hideBookATeamMember: Optional[bool] = None,
        metadata: Optional[str] = None,
        theme: Optional[str] = None,
        brandColor: Optional[str] = None,
        darkBrandColor: Optional[str] = None,
        bannerUrl: Optional[str] = None,
        timeFormat: Optional[float] = None,
        timeZone: Optional[str] = None,
        weekStart: Optional[str] = None,
        autoAcceptCreator: Optional[bool] = None,
    ) -> TeamscontrollerCreateteamresponse:
        """
        Creates a new team using the API and returns a successful response with a 201 status code, indicating the creation of a resource.

        Args:
            name (string): Name of the team Example: 'CalTeam'.
            slug (string): Team slug Example: 'caltel'.
            logoUrl (string): URL of the teams logo image Example: 'https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png'.
            calVideoLogo (string): calVideoLogo
            appLogo (string): appLogo
            appIconLogo (string): appIconLogo
            bio (string): bio
            hideBranding (boolean): hideBranding
            isPrivate (boolean): isPrivate
            hideBookATeamMember (boolean): hideBookATeamMember
            metadata (string): metadata
            theme (string): theme
            brandColor (string): brandColor
            darkBrandColor (string): darkBrandColor
            bannerUrl (string): URL of the teams banner image which is shown on booker Example: 'https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png'.
            timeFormat (number): timeFormat
            timeZone (string): Timezone is used to create teams's default schedule from Monday to Friday from 9AM to 5PM. It will default to Europe/London if not passed. Example: 'America/New_York'.
            weekStart (string): weekStart Example: 'Monday'.
            autoAcceptCreator (boolean): autoAcceptCreator

        Returns:
            TeamscontrollerCreateteamresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams
        """
        request_body_data = None
        request_body_data = {
            "name": name,
            "slug": slug,
            "logoUrl": logoUrl,
            "calVideoLogo": calVideoLogo,
            "appLogo": appLogo,
            "appIconLogo": appIconLogo,
            "bio": bio,
            "hideBranding": hideBranding,
            "isPrivate": isPrivate,
            "hideBookATeamMember": hideBookATeamMember,
            "metadata": metadata,
            "theme": theme,
            "brandColor": brandColor,
            "darkBrandColor": darkBrandColor,
            "bannerUrl": bannerUrl,
            "timeFormat": timeFormat,
            "timeZone": timeZone,
            "weekStart": weekStart,
            "autoAcceptCreator": autoAcceptCreator,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/teams"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return TeamscontrollerCreateteamresponse.model_validate(
            self._handle_response(response)
        )

    def teams_controller_get_teams(self) -> Getorganizationteamsresponse:
        """
        Retrieves a list of teams and returns their details in the response.

        Returns:
            Getorganizationteamsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams
        """
        url = f"{self.base_url}/v2/teams"
        query_params = {}
        response = self._get(url, params=query_params)
        return Getorganizationteamsresponse.model_validate(
            self._handle_response(response)
        )

    def teams_controller_get_team(
        self, teamId: str
    ) -> Createteaminorganizationresponse:
        """
        Retrieves information about a team specified by the team ID using the GET method.

        Args:
            teamId (string): teamId

        Returns:
            Createteaminorganizationresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        url = f"{self.base_url}/v2/teams/{teamId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Createteaminorganizationresponse.model_validate(
            self._handle_response(response)
        )

    def teams_controller_update_team(
        self,
        teamId: str,
        name: Optional[str] = None,
        slug: Optional[str] = None,
        logoUrl: Optional[str] = None,
        calVideoLogo: Optional[str] = None,
        appLogo: Optional[str] = None,
        appIconLogo: Optional[str] = None,
        bio: Optional[str] = None,
        hideBranding: Optional[bool] = None,
        isPrivate: Optional[bool] = None,
        hideBookATeamMember: Optional[bool] = None,
        metadata: Optional[str] = None,
        theme: Optional[str] = None,
        brandColor: Optional[str] = None,
        darkBrandColor: Optional[str] = None,
        bannerUrl: Optional[str] = None,
        timeFormat: Optional[float] = None,
        timeZone: Optional[str] = None,
        weekStart: Optional[str] = None,
        bookingLimits: Optional[str] = None,
        includeManagedEventsInLimits: Optional[bool] = None,
    ) -> Createteaminorganizationresponse:
        """
        Updates team configuration details for the specified team ID.

        Args:
            teamId (string): teamId
            name (string): Name of the team Example: 'CalTeam'.
            slug (string): Team slug Example: 'caltel'.
            logoUrl (string): URL of the teams logo image Example: 'https://i.cal.com/api/avatar/b0b58752-68ad-4c0d-8024-4fa382a77752.png'.
            calVideoLogo (string): calVideoLogo
            appLogo (string): appLogo
            appIconLogo (string): appIconLogo
            bio (string): bio
            hideBranding (boolean): hideBranding
            isPrivate (boolean): isPrivate
            hideBookATeamMember (boolean): hideBookATeamMember
            metadata (string): metadata
            theme (string): theme
            brandColor (string): brandColor
            darkBrandColor (string): darkBrandColor
            bannerUrl (string): URL of the teams banner image which is shown on booker Example: 'https://i.cal.com/api/avatar/949be534-7a88-4185-967c-c020b0c0bef3.png'.
            timeFormat (number): timeFormat
            timeZone (string): Timezone is used to create teams's default schedule from Monday to Friday from 9AM to 5PM. It will default to Europe/London if not passed. Example: 'America/New_York'.
            weekStart (string): weekStart Example: 'Monday'.
            bookingLimits (string): bookingLimits
            includeManagedEventsInLimits (boolean): includeManagedEventsInLimits

        Returns:
            Createteaminorganizationresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        request_body_data = None
        request_body_data = {
            "name": name,
            "slug": slug,
            "logoUrl": logoUrl,
            "calVideoLogo": calVideoLogo,
            "appLogo": appLogo,
            "appIconLogo": appIconLogo,
            "bio": bio,
            "hideBranding": hideBranding,
            "isPrivate": isPrivate,
            "hideBookATeamMember": hideBookATeamMember,
            "metadata": metadata,
            "theme": theme,
            "brandColor": brandColor,
            "darkBrandColor": darkBrandColor,
            "bannerUrl": bannerUrl,
            "timeFormat": timeFormat,
            "timeZone": timeZone,
            "weekStart": weekStart,
            "bookingLimits": bookingLimits,
            "includeManagedEventsInLimits": includeManagedEventsInLimits,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/teams/{teamId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Createteaminorganizationresponse.model_validate(
            self._handle_response(response)
        )

    def teams_controller_delete_team(
        self, teamId: str
    ) -> Createteaminorganizationresponse:
        """
        Deletes a specified team using the provided team ID.

        Args:
            teamId (string): teamId

        Returns:
            Createteaminorganizationresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        url = f"{self.base_url}/v2/teams/{teamId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Createteaminorganizationresponse.model_validate(
            self._handle_response(response)
        )

    def create_team_event_type(
        self,
        teamId: str,
        lengthInMinutes: float,
        lengthInMinutesOptions: List[str],
        title: str,
        slug: str,
        schedulingType: dict[str, Any],
        hosts: List[dict[str, Any]],
        description: Optional[str] = None,
        locations: Optional[List[Any]] = None,
        bookingFields: Optional[List[Any]] = None,
        disableGuests: Optional[bool] = None,
        slotInterval: Optional[float] = None,
        minimumBookingNotice: Optional[float] = None,
        beforeEventBuffer: Optional[float] = None,
        afterEventBuffer: Optional[float] = None,
        scheduleId: Optional[float] = None,
        bookingLimitsCount: Optional[Any] = None,
        onlyShowFirstAvailableSlot: Optional[bool] = None,
        bookingLimitsDuration: Optional[Any] = None,
        bookingWindow: Optional[Any] = None,
        offsetStart: Optional[float] = None,
        bookerLayouts: Optional[Any] = None,
        confirmationPolicy: Optional[Any] = None,
        recurrence: Optional[Any] = None,
        requiresBookerEmailVerification: Optional[bool] = None,
        hideCalendarNotes: Optional[bool] = None,
        lockTimeZoneToggleOnBookingPage: Optional[bool] = None,
        color: Optional[dict[str, Any]] = None,
        seats: Optional[Any] = None,
        customName: Optional[str] = None,
        destinationCalendar: Optional[dict[str, Any]] = None,
        useDestinationCalendarEmail: Optional[bool] = None,
        hideCalendarEventDetails: Optional[bool] = None,
        successRedirectUrl: Optional[str] = None,
        assignAllTeamMembers: Optional[bool] = None,
    ) -> Createeventtyperesponse:
        """
        Creates a new event type for a specified team using the API and returns a successful creation status.

        Args:
            teamId (string): teamId
            lengthInMinutes (number): lengthInMinutes Example: '60'.
            lengthInMinutesOptions (array): If you want that user can choose between different lengths of the event you can specify them here. Must include the provided `lengthInMinutes`. Example: '[15, 30, 60]'.
            title (string): title Example: 'Learn the secrets of masterchief!'.
            slug (string): slug Example: 'learn-the-secrets-of-masterchief'.
            schedulingType (object): schedulingType
            hosts (array): hosts
            description (string): description Example: 'Discover the culinary wonders of the Argentina by making the best flan ever!'.
            locations (array): Locations where the event will take place. If not provided, cal video link will be used as the location.
            bookingFields (array): Custom fields that can be added to the booking form when the event is booked by someone. By default booking form has name and email field.
            disableGuests (boolean): If true, person booking this event't cant add guests via their emails.
            slotInterval (number): Number representing length of each slot when event is booked. By default it equal length of the event type.
              If event length is 60 minutes then we would have slots 9AM, 10AM, 11AM etc. but if it was changed to 30 minutes then
              we would have slots 9AM, 9:30AM, 10AM, 10:30AM etc. as the available times to book the 60 minute event.
            minimumBookingNotice (number): Minimum number of minutes before the event that a booking can be made.
            beforeEventBuffer (number): Time spaces that can be pre-pended before an event to give more time before it.
            afterEventBuffer (number): Time spaces that can be appended after an event to give more time after it.
            scheduleId (number): If you want that this event has different schedule than user's default one you can specify it here.
            bookingLimitsCount (string): Limit how many times this event can be booked
            onlyShowFirstAvailableSlot (boolean): This will limit your availability for this event type to one slot per day, scheduled at the earliest available time.
            bookingLimitsDuration (string): Limit total amount of time that this event can be booked
            bookingWindow (string): Limit how far in the future this event can be booked
            offsetStart (number): Offset timeslots shown to bookers by a specified number of minutes
            bookerLayouts (string): Should booker have week, month or column view. Specify default layout and enabled layouts user can pick.
            confirmationPolicy (string): Specify how the booking needs to be manually confirmed before it is pushed to the integrations and a confirmation mail is sent.
            recurrence (string): Create a recurring event type.
            requiresBookerEmailVerification (boolean): requiresBookerEmailVerification
            hideCalendarNotes (boolean): hideCalendarNotes
            lockTimeZoneToggleOnBookingPage (boolean): lockTimeZoneToggleOnBookingPage
            color (object): color
            seats (string): Create an event type with multiple seats.
            customName (string): Customizable event name with valid variables:
              {Event type title}, {Organiser}, {Scheduler}, {Location}, {Organiser first name},
              {Scheduler first name}, {Scheduler last name}, {Event duration}, {LOCATION},
              {HOST/ATTENDEE}, {HOST}, {ATTENDEE}, {USER} Example: '{Event type title} between {Organiser} and {Scheduler}'.
            destinationCalendar (object): destinationCalendar
            useDestinationCalendarEmail (boolean): useDestinationCalendarEmail
            hideCalendarEventDetails (boolean): hideCalendarEventDetails
            successRedirectUrl (string): A valid URL where the booker will redirect to, once the booking is completed successfully Example: 'https://masterchief.com/argentina/flan/video/9129412'.
            assignAllTeamMembers (boolean): If true, all current and future team members will be assigned to this event type

        Returns:
            Createeventtyperesponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams / Event Types
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        request_body_data = None
        request_body_data = {
            "lengthInMinutes": lengthInMinutes,
            "lengthInMinutesOptions": lengthInMinutesOptions,
            "title": title,
            "slug": slug,
            "description": description,
            "locations": locations,
            "bookingFields": bookingFields,
            "disableGuests": disableGuests,
            "slotInterval": slotInterval,
            "minimumBookingNotice": minimumBookingNotice,
            "beforeEventBuffer": beforeEventBuffer,
            "afterEventBuffer": afterEventBuffer,
            "scheduleId": scheduleId,
            "bookingLimitsCount": bookingLimitsCount,
            "onlyShowFirstAvailableSlot": onlyShowFirstAvailableSlot,
            "bookingLimitsDuration": bookingLimitsDuration,
            "bookingWindow": bookingWindow,
            "offsetStart": offsetStart,
            "bookerLayouts": bookerLayouts,
            "confirmationPolicy": confirmationPolicy,
            "recurrence": recurrence,
            "requiresBookerEmailVerification": requiresBookerEmailVerification,
            "hideCalendarNotes": hideCalendarNotes,
            "lockTimeZoneToggleOnBookingPage": lockTimeZoneToggleOnBookingPage,
            "color": color,
            "seats": seats,
            "customName": customName,
            "destinationCalendar": destinationCalendar,
            "useDestinationCalendarEmail": useDestinationCalendarEmail,
            "hideCalendarEventDetails": hideCalendarEventDetails,
            "successRedirectUrl": successRedirectUrl,
            "schedulingType": schedulingType,
            "hosts": hosts,
            "assignAllTeamMembers": assignAllTeamMembers,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/teams/{teamId}/event-types"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createeventtyperesponse.model_validate(self._handle_response(response))

    def get_team_event_types(
        self, teamId: str, eventSlug: Optional[str] = None
    ) -> Listeventtypesbyteamandorgresponse:
        """
        Retrieves a list of event types for a specified team using the provided team ID and optionally filters by event slug.

        Args:
            teamId (string): teamId
            eventSlug (string): Slug of team event type to return.

        Returns:
            Listeventtypesbyteamandorgresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams / Event Types
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        url = f"{self.base_url}/v2/teams/{teamId}/event-types"
        query_params = {k: v for k, v in [("eventSlug", eventSlug)] if v is not None}
        response = self._get(url, params=query_params)
        return Listeventtypesbyteamandorgresponse.model_validate(
            self._handle_response(response)
        )

    def get_event_type_by_team_id(
        self, teamId: str, eventTypeId: str
    ) -> Geteventtypesbyteamidresponse:
        """
        Retrieves details about a specific event type within a team using the "GET" method, requiring both team ID and event type ID as path parameters.

        Args:
            teamId (string): teamId
            eventTypeId (string): eventTypeId

        Returns:
            Geteventtypesbyteamidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams / Event Types
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        url = f"{self.base_url}/v2/teams/{teamId}/event-types/{eventTypeId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Geteventtypesbyteamidresponse.model_validate(
            self._handle_response(response)
        )

    def delete_team_event_type_by_id(
        self, teamId: str, eventTypeId: str
    ) -> Deleteteameventtypebyidresponse:
        """
        Deletes a specific event type for a team using the provided path parameters.

        Args:
            teamId (string): teamId
            eventTypeId (string): eventTypeId

        Returns:
            Deleteteameventtypebyidresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams / Event Types
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        url = f"{self.base_url}/v2/teams/{teamId}/event-types/{eventTypeId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Deleteteameventtypebyidresponse.model_validate(
            self._handle_response(response)
        )

    def create_phone_call_for_event(
        self,
        teamId: str,
        eventTypeId: str,
        yourPhoneNumber: str,
        numberToCall: str,
        calApiKey: str,
        enabled: dict[str, Any],
        templateType: str,
        schedulerName: Optional[str] = None,
        guestName: Optional[str] = None,
        guestEmail: Optional[str] = None,
        guestCompany: Optional[str] = None,
        beginMessage: Optional[str] = None,
        generalPrompt: Optional[str] = None,
    ) -> Createphonecalleventresponse:
        """
        Creates a phone call for a specific event type within a team using the "POST" method, returning a successful creation status.

        Args:
            teamId (string): teamId
            eventTypeId (string): eventTypeId
            yourPhoneNumber (string): Your phone number
            numberToCall (string): Number to call
            calApiKey (string): CAL API Key
            enabled (object): Enabled status
            templateType (string): Template type
            schedulerName (string): Scheduler name
            guestName (string): Guest name
            guestEmail (string): Guest email
            guestCompany (string): Guest company
            beginMessage (string): Begin message
            generalPrompt (string): General prompt

        Returns:
            Createphonecalleventresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams / Event Types
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if eventTypeId is None:
            raise ValueError("Missing required parameter 'eventTypeId'.")
        request_body_data = None
        request_body_data = {
            "yourPhoneNumber": yourPhoneNumber,
            "numberToCall": numberToCall,
            "calApiKey": calApiKey,
            "enabled": enabled,
            "templateType": templateType,
            "schedulerName": schedulerName,
            "guestName": guestName,
            "guestEmail": guestEmail,
            "guestCompany": guestCompany,
            "beginMessage": beginMessage,
            "generalPrompt": generalPrompt,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/teams/{teamId}/event-types/{eventTypeId}/create-phone-call"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createphonecalleventresponse.model_validate(
            self._handle_response(response)
        )

    def add_team_membership(
        self,
        teamId: str,
        userId: float,
        accepted: Optional[bool] = None,
        role: Optional[str] = None,
        disableImpersonation: Optional[bool] = None,
    ) -> Listorganizationmembershipsresponse:
        """
        Adds multiple users to a team using their organization membership IDs through a POST request to the specified team endpoint.

        Args:
            teamId (string): teamId
            userId (number): userId
            accepted (boolean): accepted
            role (string): role
            disableImpersonation (boolean): disableImpersonation

        Returns:
            Listorganizationmembershipsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams / Memberships
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        request_body_data = None
        request_body_data = {
            "userId": userId,
            "accepted": accepted,
            "role": role,
            "disableImpersonation": disableImpersonation,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/teams/{teamId}/memberships"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Listorganizationmembershipsresponse.model_validate(
            self._handle_response(response)
        )

    def get_team_memberships(
        self, teamId: str, take: Optional[float] = None, skip: Optional[float] = None
    ) -> Listorganizationmembershipsresponse:
        """
        Retrieves paginated membership details for a specific team using `take` and `skip` parameters to manage results.

        Args:
            teamId (string): teamId
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            Listorganizationmembershipsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams / Memberships
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        url = f"{self.base_url}/v2/teams/{teamId}/memberships"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return Listorganizationmembershipsresponse.model_validate(
            self._handle_response(response)
        )

    def get_membership_by_id(
        self, teamId: str, membershipId: str
    ) -> Listorganizationmembershipsresponse:
        """
        Retrieves the membership details for a specific user in a team using the provided membership ID.

        Args:
            teamId (string): teamId
            membershipId (string): membershipId

        Returns:
            Listorganizationmembershipsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams / Memberships
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if membershipId is None:
            raise ValueError("Missing required parameter 'membershipId'.")
        url = f"{self.base_url}/v2/teams/{teamId}/memberships/{membershipId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Listorganizationmembershipsresponse.model_validate(
            self._handle_response(response)
        )

    def update_membership(
        self,
        teamId: str,
        membershipId: str,
        accepted: Optional[bool] = None,
        role: Optional[str] = None,
        disableImpersonation: Optional[bool] = None,
    ) -> Listorganizationmembershipsresponse:
        """
        Updates the membership role for a user in a specific team using the GitHub API and returns a success status.

        Args:
            teamId (string): teamId
            membershipId (string): membershipId
            accepted (boolean): accepted
            role (string): role
            disableImpersonation (boolean): disableImpersonation

        Returns:
            Listorganizationmembershipsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams / Memberships
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if membershipId is None:
            raise ValueError("Missing required parameter 'membershipId'.")
        request_body_data = None
        request_body_data = {
            "accepted": accepted,
            "role": role,
            "disableImpersonation": disableImpersonation,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/teams/{teamId}/memberships/{membershipId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Listorganizationmembershipsresponse.model_validate(
            self._handle_response(response)
        )

    def deletegithub_membership_by_id(
        self, teamId: str, membershipId: str
    ) -> Listorganizationmembershipsresponse:
        """
        Removes a user's team membership in GitHub, requiring admin permissions or organization ownership.

        Args:
            teamId (string): teamId
            membershipId (string): membershipId

        Returns:
            Listorganizationmembershipsresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Teams / Memberships
        """
        if teamId is None:
            raise ValueError("Missing required parameter 'teamId'.")
        if membershipId is None:
            raise ValueError("Missing required parameter 'membershipId'.")
        url = f"{self.base_url}/v2/teams/{teamId}/memberships/{membershipId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Listorganizationmembershipsresponse.model_validate(
            self._handle_response(response)
        )

    def get_timezones(self) -> Checkicsfeedresponse:
        """
        Retrieves a list of time zones with associated metadata, including codes, descriptions, and identifiers.

        Returns:
            Checkicsfeedresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Timezones
        """
        url = f"{self.base_url}/v2/timezones"
        query_params = {}
        response = self._get(url, params=query_params)
        return Checkicsfeedresponse.model_validate(self._handle_response(response))

    def createandconfigure_webhook(
        self,
        active: bool,
        subscriberUrl: str,
        triggers: str,
        payloadTemplate: Optional[str] = None,
        secret: Optional[str] = None,
    ) -> Createandconfigurewebhookresponse:
        """
        Creates and configures a webhook endpoint to receive HTTP POST notifications for specific events, returning a success response upon creation.

        Args:
            active (boolean): active
            subscriberUrl (string): subscriberUrl
            triggers (string): triggers Example: "['BOOKING_CREATED', 'BOOKING_RESCHEDULED', 'BOOKING_CANCELLED', 'BOOKING_CONFIRMED', 'BOOKING_REJECTED', 'BOOKING_COMPLETED', 'BOOKING_NO_SHOW', 'BOOKING_REOPENED']".
            payloadTemplate (string): The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information Example: '{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}'.
            secret (string): secret

        Returns:
            Createandconfigurewebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Webhooks
        """
        request_body_data = None
        request_body_data = {
            "payloadTemplate": payloadTemplate,
            "active": active,
            "subscriberUrl": subscriberUrl,
            "triggers": triggers,
            "secret": secret,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/webhooks"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return Createandconfigurewebhookresponse.model_validate(
            self._handle_response(response)
        )

    def webhooks_controller_get_webhooks(
        self, take: Optional[float] = None, skip: Optional[float] = None
    ) -> WebhookscontrollerGetwebhooksresponse:
        """
        Retrieves a list of webhooks, allowing pagination with optional parameters to specify the number of items to take and skip.

        Args:
            take (number): The number of items to return Example: '10'.
            skip (number): The number of items to skip Example: '0'.

        Returns:
            WebhookscontrollerGetwebhooksresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Webhooks
        """
        url = f"{self.base_url}/v2/webhooks"
        query_params = {
            k: v for k, v in [("take", take), ("skip", skip)] if v is not None
        }
        response = self._get(url, params=query_params)
        return WebhookscontrollerGetwebhooksresponse.model_validate(
            self._handle_response(response)
        )

    def patch_webhook(
        self,
        webhookId: str,
        payloadTemplate: Optional[str] = None,
        active: Optional[bool] = None,
        subscriberUrl: Optional[str] = None,
        triggers: Optional[str] = None,
        secret: Optional[str] = None,
    ) -> Createandconfigurewebhookresponse:
        """
        Updates a webhook identified by its ID using the PATCH method to modify its configuration.

        Args:
            webhookId (string): webhookId
            payloadTemplate (string): The template of the payload that will be sent to the subscriberUrl, check cal.com/docs/core-features/webhooks for more information Example: '{"content":"A new event has been scheduled","type":"{{type}}","name":"{{title}}","organizer":"{{organizer.name}}","booker":"{{attendees.0.name}}"}'.
            active (boolean): active
            subscriberUrl (string): subscriberUrl
            triggers (string): triggers Example: "['BOOKING_CREATED', 'BOOKING_RESCHEDULED', 'BOOKING_CANCELLED', 'BOOKING_CONFIRMED', 'BOOKING_REJECTED', 'BOOKING_COMPLETED', 'BOOKING_NO_SHOW', 'BOOKING_REOPENED']".
            secret (string): secret

        Returns:
            Createandconfigurewebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Webhooks
        """
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        request_body_data = None
        request_body_data = {
            "payloadTemplate": payloadTemplate,
            "active": active,
            "subscriberUrl": subscriberUrl,
            "triggers": triggers,
            "secret": secret,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.base_url}/v2/webhooks/{webhookId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return Createandconfigurewebhookresponse.model_validate(
            self._handle_response(response)
        )

    def webhooks_controller_get_webhook(
        self, webhookId: str
    ) -> Createandconfigurewebhookresponse:
        """
        Retrieves information about a specific webhook identified by its ID using the "GET" method.

        Args:
            webhookId (string): webhookId

        Returns:
            Createandconfigurewebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Webhooks
        """
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        url = f"{self.base_url}/v2/webhooks/{webhookId}"
        query_params = {}
        response = self._get(url, params=query_params)
        return Createandconfigurewebhookresponse.model_validate(
            self._handle_response(response)
        )

    def delete_user_webhook_by_id(
        self, webhookId: str
    ) -> Createandconfigurewebhookresponse:
        """
        Deletes a webhook by its ID using the DELETE method at the "/v2/webhooks/{webhookId}" path, removing the specified webhook endpoint.

        Args:
            webhookId (string): webhookId

        Returns:
            Createandconfigurewebhookresponse: API response data.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            Webhooks
        """
        if webhookId is None:
            raise ValueError("Missing required parameter 'webhookId'.")
        url = f"{self.base_url}/v2/webhooks/{webhookId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return Createandconfigurewebhookresponse.model_validate(
            self._handle_response(response)
        )

    def list_tools(self):
        return [
            self.get_provider_details,
            self.get_provider_access_token,
            self.gcal_controller_redirect,
            self.gcal_controller_save,
            self.gcal_controller_check,
            self.list_client_users,
            self.create_oauth_client_user,
            self.get_oauth_client_user_by_id,
            self.patch_oauth_client_user_by_id,
            self.delete_user_by_client_id_id,
            self.force_refresh_user,
            self.refresh_oauth_client_token,
            self.create_oauth_client_webhook,
            self.list_webhooks_by_client_id,
            self.delete_client_webhook,
            self.update_webhook,
            self.get_oauth_client_webhook_by_id,
            self.delete_oauth_client_webhook_by_id,
            self.list_org_attributes,
            self.create_org_attributes,
            self.fetch_organization_attribute_by_id,
            self.update_organization_attribute,
            self.delete_org_attribute,
            self.create_org_attribute_option,
            self.get_org_attribute_options,
            self.delete_attribute_option_by_id,
            self.patch_option_by_id,
            self.set_user_attribute_option,
            self.get_user_org_attribute_options,
            self.delete_attribute_option,
            self.create_event_type,
            self.list_event_types_by_team_and_org,
            self.get_event_types_by_team_id,
            self.create_phone_call_event,
            self.list_event_types_by_org_id,
            self.list_organization_memberships,
            self.create_membership,
            self.get_org_membership_by_id,
            self.delete_org_membership_by_id,
            self.update_membership_by_id_org,
            self.get_organization_schedules,
            self.create_user_schedule,
            self.get_user_schedule,
            self.get_schedule_detail,
            self.update_user_schedule_by_id,
            self.delete_user_schedule_by_id,
            self.get_organization_teams,
            self.create_team_in_organization,
            self.get_organization_team_me,
            self.get_organization_team_by_id,
            self.delete_team_by_id,
            self.update_team,
            self.list_team_memberships,
            self.create_team_membership,
            self.get_membership_details,
            self.delete_org_team_membership_by_id,
            self.patch_team_membership_by_id,
            self.get_schedule_by_user,
            self.list_org_users,
            self.create_org_user,
            self.delete_member_by_id,
            self.get_org_webhooks,
            self.create_webhook,
            self.get_organization_webhook_by_id,
            self.delete_organization_webhook_by_id,
            self.update_webhook_by_id,
            self.list_bookings,
            self.get_booking_by_uid,
            self.reschedule_booking_by_uid,
            self.cancel_booking_by_uid,
            self.mark_booking_absent_by_uid,
            self.reassign_booking,
            self.reassign_booking_to_user,
            self.confirm_booking,
            self.decline_booking,
            self.save_ics_feed_post,
            self.check_ics_feed,
            self.get_calendars_busy_times,
            self.get_calendars,
            self.calendars_controller_redirect,
            self.calendars_controller_save,
            self.create_calendar_credentials,
            self.calendars_controller_check,
            self.disconnect_calendar,
            self.conferencing_controller_connect,
            self.get_auth_url,
            self.conferencing_controller_save,
            self.list_conferencing,
            self.conferencing_controller_default,
            self.get_default_conferencing,
            self.disconnect_conferencing_app,
            self.update_destination_calendars,
            self.list_event_types,
            self.get_event_type_by_id,
            self.delete_event_type_by_id,
            self.create_event_type_webhook,
            self.get_event_webhooks,
            self.delete_event_webhook,
            self.patch_event_type_webhook_by_id,
            self.get_webhook_by_id,
            self.delete_event_type_webhook_by_id,
            self.me_controller_get_me,
            self.me_controller_update_me,
            self.create_schedule,
            self.list_schedules,
            self.get_default_schedule,
            self.get_schedule_by_id,
            self.update_schedule_by_id,
            self.delete_schedule_by_id,
            self.add_selected_calendar,
            self.delete_selected_calendars,
            self.slots_controller_reserve_slot,
            self.delete_selected_slot,
            self.list_available_slots,
            self.stripe_controller_redirect,
            self.stripe_controller_save,
            self.stripe_controller_check,
            self.get_team_stripe_check,
            self.teams_controller_create_team,
            self.teams_controller_get_teams,
            self.teams_controller_get_team,
            self.teams_controller_update_team,
            self.teams_controller_delete_team,
            self.create_team_event_type,
            self.get_team_event_types,
            self.get_event_type_by_team_id,
            self.delete_team_event_type_by_id,
            self.create_phone_call_for_event,
            self.add_team_membership,
            self.get_team_memberships,
            self.get_membership_by_id,
            self.update_membership,
            self.deletegithub_membership_by_id,
            self.get_timezones,
            self.createandconfigure_webhook,
            self.webhooks_controller_get_webhooks,
            self.patch_webhook,
            self.webhooks_controller_get_webhook,
            self.delete_user_webhook_by_id,
        ]
