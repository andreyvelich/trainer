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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow_trainer_api.models.io_k8s_api_core_v1_pod_template_spec import IoK8sApiCoreV1PodTemplateSpec
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1ReplicationControllerSpec(BaseModel):
    """
    ReplicationControllerSpec is the specification of a replication controller.
    """ # noqa: E501
    min_ready_seconds: Optional[StrictInt] = Field(default=0, description="Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)", alias="minReadySeconds")
    replicas: Optional[StrictInt] = Field(default=1, description="Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller")
    selector: Optional[Dict[str, StrictStr]] = Field(default=None, description="Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors")
    template: Optional[IoK8sApiCoreV1PodTemplateSpec] = Field(default=None, description="Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. The only allowed template.spec.restartPolicy value is \"Always\". More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template")
    __properties: ClassVar[List[str]] = ["minReadySeconds", "replicas", "selector", "template"]

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
        """Create an instance of IoK8sApiCoreV1ReplicationControllerSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1ReplicationControllerSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "minReadySeconds": obj.get("minReadySeconds") if obj.get("minReadySeconds") is not None else 0,
            "replicas": obj.get("replicas") if obj.get("replicas") is not None else 1,
            "selector": obj.get("selector"),
            "template": IoK8sApiCoreV1PodTemplateSpec.from_dict(obj["template"]) if obj.get("template") is not None else None
        })
        return _obj


