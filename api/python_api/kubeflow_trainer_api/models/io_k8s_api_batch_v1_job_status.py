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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kubeflow_trainer_api.models.io_k8s_api_batch_v1_job_condition import IoK8sApiBatchV1JobCondition
from kubeflow_trainer_api.models.io_k8s_api_batch_v1_uncounted_terminated_pods import IoK8sApiBatchV1UncountedTerminatedPods
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiBatchV1JobStatus(BaseModel):
    """
    JobStatus represents the current state of a Job.
    """ # noqa: E501
    active: Optional[StrictInt] = Field(default=None, description="The number of pending and running pods which are not terminating (without a deletionTimestamp). The value is zero for finished jobs.")
    completed_indexes: Optional[StrictStr] = Field(default=None, description="completedIndexes holds the completed indexes when .spec.completionMode = \"Indexed\" in a text format. The indexes are represented as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the completed indexes are 1, 3, 4, 5 and 7, they are represented as \"1,3-5,7\".", alias="completedIndexes")
    completion_time: Optional[datetime] = Field(default=None, description="Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. The completion time is set when the job finishes successfully, and only then. The value cannot be updated or removed. The value indicates the same or later point in time as the startTime field.", alias="completionTime")
    conditions: Optional[List[IoK8sApiBatchV1JobCondition]] = Field(default=None, description="The latest available observations of an object's current state. When a Job fails, one of the conditions will have type \"Failed\" and status true. When a Job is suspended, one of the conditions will have type \"Suspended\" and status true; when the Job is resumed, the status of this condition will become false. When a Job is completed, one of the conditions will have type \"Complete\" and status true.  A job is considered finished when it is in a terminal condition, either \"Complete\" or \"Failed\". A Job cannot have both the \"Complete\" and \"Failed\" conditions. Additionally, it cannot be in the \"Complete\" and \"FailureTarget\" conditions. The \"Complete\", \"Failed\" and \"FailureTarget\" conditions cannot be disabled.  More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/")
    failed: Optional[StrictInt] = Field(default=None, description="The number of pods which reached phase Failed. The value increases monotonically.")
    failed_indexes: Optional[StrictStr] = Field(default=None, description="FailedIndexes holds the failed indexes when spec.backoffLimitPerIndex is set. The indexes are represented in the text format analogous as for the `completedIndexes` field, ie. they are kept as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the failed indexes are 1, 3, 4, 5 and 7, they are represented as \"1,3-5,7\". The set of failed indexes cannot overlap with the set of completed indexes.", alias="failedIndexes")
    ready: Optional[StrictInt] = Field(default=None, description="The number of active pods which have a Ready condition and are not terminating (without a deletionTimestamp).")
    start_time: Optional[datetime] = Field(default=None, description="Represents time when the job controller started processing a job. When a Job is created in the suspended state, this field is not set until the first time it is resumed. This field is reset every time a Job is resumed from suspension. It is represented in RFC3339 form and is in UTC.  Once set, the field can only be removed when the job is suspended. The field cannot be modified while the job is unsuspended or finished.", alias="startTime")
    succeeded: Optional[StrictInt] = Field(default=None, description="The number of pods which reached phase Succeeded. The value increases monotonically for a given spec. However, it may decrease in reaction to scale down of elastic indexed jobs.")
    terminating: Optional[StrictInt] = Field(default=None, description="The number of pods which are terminating (in phase Pending or Running and have a deletionTimestamp).  This field is beta-level. The job controller populates the field when the feature gate JobPodReplacementPolicy is enabled (enabled by default).")
    uncounted_terminated_pods: Optional[IoK8sApiBatchV1UncountedTerminatedPods] = Field(default=None, description="uncountedTerminatedPods holds the UIDs of Pods that have terminated but the job controller hasn't yet accounted for in the status counters.  The job controller creates pods with a finalizer. When a pod terminates (succeeded or failed), the controller does three steps to account for it in the job status:  1. Add the pod UID to the arrays in this field. 2. Remove the pod finalizer. 3. Remove the pod UID from the arrays while increasing the corresponding     counter.  Old jobs might not be tracked using this field, in which case the field remains null. The structure is empty for finished jobs.", alias="uncountedTerminatedPods")
    __properties: ClassVar[List[str]] = ["active", "completedIndexes", "completionTime", "conditions", "failed", "failedIndexes", "ready", "startTime", "succeeded", "terminating", "uncountedTerminatedPods"]

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
        """Create an instance of IoK8sApiBatchV1JobStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item_conditions in self.conditions:
                if _item_conditions:
                    _items.append(_item_conditions.to_dict())
            _dict['conditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of uncounted_terminated_pods
        if self.uncounted_terminated_pods:
            _dict['uncountedTerminatedPods'] = self.uncounted_terminated_pods.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiBatchV1JobStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "completedIndexes": obj.get("completedIndexes"),
            "completionTime": obj.get("completionTime"),
            "conditions": [IoK8sApiBatchV1JobCondition.from_dict(_item) for _item in obj["conditions"]] if obj.get("conditions") is not None else None,
            "failed": obj.get("failed"),
            "failedIndexes": obj.get("failedIndexes"),
            "ready": obj.get("ready"),
            "startTime": obj.get("startTime"),
            "succeeded": obj.get("succeeded"),
            "terminating": obj.get("terminating"),
            "uncountedTerminatedPods": IoK8sApiBatchV1UncountedTerminatedPods.from_dict(obj["uncountedTerminatedPods"]) if obj.get("uncountedTerminatedPods") is not None else None
        })
        return _obj


