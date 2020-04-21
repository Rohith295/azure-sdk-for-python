# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class PublicAccessType(str, Enum):

    container = "container"
    blob = "blob"


class CopyStatusType(str, Enum):

    pending = "pending"
    success = "success"
    aborted = "aborted"
    failed = "failed"


class LeaseDurationType(str, Enum):

    infinite = "infinite"
    fixed = "fixed"


class LeaseStateType(str, Enum):

    available = "available"
    leased = "leased"
    expired = "expired"
    breaking = "breaking"
    broken = "broken"


class LeaseStatusType(str, Enum):

    locked = "locked"
    unlocked = "unlocked"


class AccessTier(str, Enum):

    p4 = "P4"
    p6 = "P6"
    p10 = "P10"
    p15 = "P15"
    p20 = "P20"
    p30 = "P30"
    p40 = "P40"
    p50 = "P50"
    p60 = "P60"
    p70 = "P70"
    p80 = "P80"
    hot = "Hot"
    cool = "Cool"
    archive = "Archive"


class ArchiveStatus(str, Enum):

    rehydrate_pending_to_hot = "rehydrate-pending-to-hot"
    rehydrate_pending_to_cool = "rehydrate-pending-to-cool"


class BlobType(str, Enum):

    block_blob = "BlockBlob"
    page_blob = "PageBlob"
    append_blob = "AppendBlob"


class StorageErrorCode(str, Enum):

    account_already_exists = "AccountAlreadyExists"
    account_being_created = "AccountBeingCreated"
    account_is_disabled = "AccountIsDisabled"
    authentication_failed = "AuthenticationFailed"
    authorization_failure = "AuthorizationFailure"
    condition_headers_not_supported = "ConditionHeadersNotSupported"
    condition_not_met = "ConditionNotMet"
    empty_metadata_key = "EmptyMetadataKey"
    insufficient_account_permissions = "InsufficientAccountPermissions"
    internal_error = "InternalError"
    invalid_authentication_info = "InvalidAuthenticationInfo"
    invalid_header_value = "InvalidHeaderValue"
    invalid_http_verb = "InvalidHttpVerb"
    invalid_input = "InvalidInput"
    invalid_md5 = "InvalidMd5"
    invalid_metadata = "InvalidMetadata"
    invalid_query_parameter_value = "InvalidQueryParameterValue"
    invalid_range = "InvalidRange"
    invalid_resource_name = "InvalidResourceName"
    invalid_uri = "InvalidUri"
    invalid_xml_document = "InvalidXmlDocument"
    invalid_xml_node_value = "InvalidXmlNodeValue"
    md5_mismatch = "Md5Mismatch"
    metadata_too_large = "MetadataTooLarge"
    missing_content_length_header = "MissingContentLengthHeader"
    missing_required_query_parameter = "MissingRequiredQueryParameter"
    missing_required_header = "MissingRequiredHeader"
    missing_required_xml_node = "MissingRequiredXmlNode"
    multiple_condition_headers_not_supported = "MultipleConditionHeadersNotSupported"
    operation_timed_out = "OperationTimedOut"
    out_of_range_input = "OutOfRangeInput"
    out_of_range_query_parameter_value = "OutOfRangeQueryParameterValue"
    request_body_too_large = "RequestBodyTooLarge"
    resource_type_mismatch = "ResourceTypeMismatch"
    request_url_failed_to_parse = "RequestUrlFailedToParse"
    resource_already_exists = "ResourceAlreadyExists"
    resource_not_found = "ResourceNotFound"
    server_busy = "ServerBusy"
    unsupported_header = "UnsupportedHeader"
    unsupported_xml_node = "UnsupportedXmlNode"
    unsupported_query_parameter = "UnsupportedQueryParameter"
    unsupported_http_verb = "UnsupportedHttpVerb"
    append_position_condition_not_met = "AppendPositionConditionNotMet"
    blob_already_exists = "BlobAlreadyExists"
    blob_not_found = "BlobNotFound"
    blob_overwritten = "BlobOverwritten"
    blob_tier_inadequate_for_content_length = "BlobTierInadequateForContentLength"
    block_count_exceeds_limit = "BlockCountExceedsLimit"
    block_list_too_long = "BlockListTooLong"
    cannot_change_to_lower_tier = "CannotChangeToLowerTier"
    cannot_verify_copy_source = "CannotVerifyCopySource"
    container_already_exists = "ContainerAlreadyExists"
    container_being_deleted = "ContainerBeingDeleted"
    container_disabled = "ContainerDisabled"
    container_not_found = "ContainerNotFound"
    content_length_larger_than_tier_limit = "ContentLengthLargerThanTierLimit"
    copy_across_accounts_not_supported = "CopyAcrossAccountsNotSupported"
    copy_id_mismatch = "CopyIdMismatch"
    feature_version_mismatch = "FeatureVersionMismatch"
    incremental_copy_blob_mismatch = "IncrementalCopyBlobMismatch"
    incremental_copy_of_eralier_version_snapshot_not_allowed = "IncrementalCopyOfEralierVersionSnapshotNotAllowed"
    incremental_copy_source_must_be_snapshot = "IncrementalCopySourceMustBeSnapshot"
    infinite_lease_duration_required = "InfiniteLeaseDurationRequired"
    invalid_blob_or_block = "InvalidBlobOrBlock"
    invalid_blob_tier = "InvalidBlobTier"
    invalid_blob_type = "InvalidBlobType"
    invalid_block_id = "InvalidBlockId"
    invalid_block_list = "InvalidBlockList"
    invalid_operation = "InvalidOperation"
    invalid_page_range = "InvalidPageRange"
    invalid_source_blob_type = "InvalidSourceBlobType"
    invalid_source_blob_url = "InvalidSourceBlobUrl"
    invalid_version_for_page_blob_operation = "InvalidVersionForPageBlobOperation"
    lease_already_present = "LeaseAlreadyPresent"
    lease_already_broken = "LeaseAlreadyBroken"
    lease_id_mismatch_with_blob_operation = "LeaseIdMismatchWithBlobOperation"
    lease_id_mismatch_with_container_operation = "LeaseIdMismatchWithContainerOperation"
    lease_id_mismatch_with_lease_operation = "LeaseIdMismatchWithLeaseOperation"
    lease_id_missing = "LeaseIdMissing"
    lease_is_breaking_and_cannot_be_acquired = "LeaseIsBreakingAndCannotBeAcquired"
    lease_is_breaking_and_cannot_be_changed = "LeaseIsBreakingAndCannotBeChanged"
    lease_is_broken_and_cannot_be_renewed = "LeaseIsBrokenAndCannotBeRenewed"
    lease_lost = "LeaseLost"
    lease_not_present_with_blob_operation = "LeaseNotPresentWithBlobOperation"
    lease_not_present_with_container_operation = "LeaseNotPresentWithContainerOperation"
    lease_not_present_with_lease_operation = "LeaseNotPresentWithLeaseOperation"
    max_blob_size_condition_not_met = "MaxBlobSizeConditionNotMet"
    no_authentication_information = "NoAuthenticationInformation"
    no_pending_copy_operation = "NoPendingCopyOperation"
    operation_not_allowed_on_incremental_copy_blob = "OperationNotAllowedOnIncrementalCopyBlob"
    pending_copy_operation = "PendingCopyOperation"
    previous_snapshot_cannot_be_newer = "PreviousSnapshotCannotBeNewer"
    previous_snapshot_not_found = "PreviousSnapshotNotFound"
    previous_snapshot_operation_not_supported = "PreviousSnapshotOperationNotSupported"
    sequence_number_condition_not_met = "SequenceNumberConditionNotMet"
    sequence_number_increment_too_large = "SequenceNumberIncrementTooLarge"
    snapshot_count_exceeded = "SnapshotCountExceeded"
    snaphot_operation_rate_exceeded = "SnaphotOperationRateExceeded"
    snapshots_present = "SnapshotsPresent"
    source_condition_not_met = "SourceConditionNotMet"
    system_in_use = "SystemInUse"
    target_condition_not_met = "TargetConditionNotMet"
    unauthorized_blob_overwrite = "UnauthorizedBlobOverwrite"
    blob_being_rehydrated = "BlobBeingRehydrated"
    blob_archived = "BlobArchived"
    blob_not_archived = "BlobNotArchived"
    authorization_source_ip_mismatch = "AuthorizationSourceIPMismatch"
    authorization_protocol_mismatch = "AuthorizationProtocolMismatch"
    authorization_permission_mismatch = "AuthorizationPermissionMismatch"
    authorization_service_mismatch = "AuthorizationServiceMismatch"
    authorization_resource_type_mismatch = "AuthorizationResourceTypeMismatch"


class GeoReplicationStatusType(str, Enum):

    live = "live"
    bootstrap = "bootstrap"
    unavailable = "unavailable"


class QuickQueryFormatType(str, Enum):

    delimited = "delimited"
    json = "json"


class AccessTierRequired(str, Enum):

    p4 = "P4"
    p6 = "P6"
    p10 = "P10"
    p15 = "P15"
    p20 = "P20"
    p30 = "P30"
    p40 = "P40"
    p50 = "P50"
    p60 = "P60"
    p70 = "P70"
    p80 = "P80"
    hot = "Hot"
    cool = "Cool"
    archive = "Archive"


class AccessTierOptional(str, Enum):

    p4 = "P4"
    p6 = "P6"
    p10 = "P10"
    p15 = "P15"
    p20 = "P20"
    p30 = "P30"
    p40 = "P40"
    p50 = "P50"
    p60 = "P60"
    p70 = "P70"
    p80 = "P80"
    hot = "Hot"
    cool = "Cool"
    archive = "Archive"


class PremiumPageBlobAccessTier(str, Enum):

    p4 = "P4"
    p6 = "P6"
    p10 = "P10"
    p15 = "P15"
    p20 = "P20"
    p30 = "P30"
    p40 = "P40"
    p50 = "P50"
    p60 = "P60"
    p70 = "P70"
    p80 = "P80"


class RehydratePriority(str, Enum):

    high = "High"
    standard = "Standard"


class BlobExpiryOptions(str, Enum):

    never_expire = "NeverExpire"
    relative_to_creation = "RelativeToCreation"
    relative_to_now = "RelativeToNow"
    absolute = "Absolute"


class BlockListType(str, Enum):

    committed = "committed"
    uncommitted = "uncommitted"
    all = "all"


class DeleteSnapshotsOptionType(str, Enum):

    include = "include"
    only = "only"


class EncryptionAlgorithmType(str, Enum):

    aes256 = "AES256"


class ListBlobsIncludeItem(str, Enum):

    copy = "copy"
    deleted = "deleted"
    metadata = "metadata"
    snapshots = "snapshots"
    uncommittedblobs = "uncommittedblobs"
    versions = "versions"
    tags = "tags"


class ListContainersIncludeType(str, Enum):

    metadata = "metadata"
    deleted = "deleted"


class PathRenameMode(str, Enum):

    legacy = "legacy"
    posix = "posix"


class SequenceNumberActionType(str, Enum):

    max = "max"
    update = "update"
    increment = "increment"


class SkuName(str, Enum):

    standard_lrs = "Standard_LRS"
    standard_grs = "Standard_GRS"
    standard_ragrs = "Standard_RAGRS"
    standard_zrs = "Standard_ZRS"
    premium_lrs = "Premium_LRS"


class AccountKind(str, Enum):

    storage = "Storage"
    blob_storage = "BlobStorage"
    storage_v2 = "StorageV2"


class SyncCopyStatusType(str, Enum):

    success = "success"
