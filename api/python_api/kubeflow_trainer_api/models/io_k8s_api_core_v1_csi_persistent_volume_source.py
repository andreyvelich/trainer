# coding: utf-8

"""
    Kubeflow Trainer OpenAPI Spec

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: unversioned
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow_trainer_api.models.io_k8s_api_core_v1_secret_reference import IoK8sApiCoreV1SecretReference
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1CSIPersistentVolumeSource(BaseModel):
    """
    Represents storage that is managed by an external CSI volume driver
    """ # noqa: E501
    controller_expand_secret_ref: Optional[IoK8sApiCoreV1SecretReference] = Field(default=None, description="controllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.", alias="controllerExpandSecretRef")
    controller_publish_secret_ref: Optional[IoK8sApiCoreV1SecretReference] = Field(default=None, description="controllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.", alias="controllerPublishSecretRef")
    driver: StrictStr = Field(description="driver is the name of the driver to use for this volume. Required.")
    fs_type: Optional[StrictStr] = Field(default=None, description="fsType to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\".", alias="fsType")
    node_expand_secret_ref: Optional[IoK8sApiCoreV1SecretReference] = Field(default=None, description="nodeExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeExpandVolume call. This field is optional, may be omitted if no secret is required. If the secret object contains more than one secret, all secrets are passed.", alias="nodeExpandSecretRef")
    node_publish_secret_ref: Optional[IoK8sApiCoreV1SecretReference] = Field(default=None, description="nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.", alias="nodePublishSecretRef")
    node_stage_secret_ref: Optional[IoK8sApiCoreV1SecretReference] = Field(default=None, description="nodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.", alias="nodeStageSecretRef")
    read_only: Optional[StrictBool] = Field(default=None, description="readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).", alias="readOnly")
    volume_attributes: Optional[Dict[str, StrictStr]] = Field(default=None, description="volumeAttributes of the volume to publish.", alias="volumeAttributes")
    volume_handle: StrictStr = Field(description="volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.", alias="volumeHandle")
    __properties: ClassVar[List[str]] = ["controllerExpandSecretRef", "controllerPublishSecretRef", "driver", "fsType", "nodeExpandSecretRef", "nodePublishSecretRef", "nodeStageSecretRef", "readOnly", "volumeAttributes", "volumeHandle"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1CSIPersistentVolumeSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of controller_expand_secret_ref
        if self.controller_expand_secret_ref:
            _dict['controllerExpandSecretRef'] = self.controller_expand_secret_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of controller_publish_secret_ref
        if self.controller_publish_secret_ref:
            _dict['controllerPublishSecretRef'] = self.controller_publish_secret_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of node_expand_secret_ref
        if self.node_expand_secret_ref:
            _dict['nodeExpandSecretRef'] = self.node_expand_secret_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of node_publish_secret_ref
        if self.node_publish_secret_ref:
            _dict['nodePublishSecretRef'] = self.node_publish_secret_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of node_stage_secret_ref
        if self.node_stage_secret_ref:
            _dict['nodeStageSecretRef'] = self.node_stage_secret_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1CSIPersistentVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "controllerExpandSecretRef": IoK8sApiCoreV1SecretReference.from_dict(obj["controllerExpandSecretRef"]) if obj.get("controllerExpandSecretRef") is not None else None,
            "controllerPublishSecretRef": IoK8sApiCoreV1SecretReference.from_dict(obj["controllerPublishSecretRef"]) if obj.get("controllerPublishSecretRef") is not None else None,
            "driver": obj.get("driver") if obj.get("driver") is not None else '',
            "fsType": obj.get("fsType"),
            "nodeExpandSecretRef": IoK8sApiCoreV1SecretReference.from_dict(obj["nodeExpandSecretRef"]) if obj.get("nodeExpandSecretRef") is not None else None,
            "nodePublishSecretRef": IoK8sApiCoreV1SecretReference.from_dict(obj["nodePublishSecretRef"]) if obj.get("nodePublishSecretRef") is not None else None,
            "nodeStageSecretRef": IoK8sApiCoreV1SecretReference.from_dict(obj["nodeStageSecretRef"]) if obj.get("nodeStageSecretRef") is not None else None,
            "readOnly": obj.get("readOnly"),
            "volumeAttributes": obj.get("volumeAttributes"),
            "volumeHandle": obj.get("volumeHandle") if obj.get("volumeHandle") is not None else ''
        })
        return _obj


