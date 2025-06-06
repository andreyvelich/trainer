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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class JobsetV1alpha2FailurePolicyRule(BaseModel):
    """
    FailurePolicyRule defines a FailurePolicyAction to be executed if a child job fails due to a reason listed in OnJobFailureReasons.
    """ # noqa: E501
    action: StrictStr = Field(description="The action to take if the rule is matched.")
    name: StrictStr = Field(description="The name of the failure policy rule. The name is defaulted to 'failurePolicyRuleN' where N is the index of the failure policy rule. The name must match the regular expression \"^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$\".")
    on_job_failure_reasons: Optional[List[StrictStr]] = Field(default=None, description="The requirement on the job failure reasons. The requirement is satisfied if at least one reason matches the list. The rules are evaluated in order, and the first matching rule is executed. An empty list applies the rule to any job failure reason.", alias="onJobFailureReasons")
    target_replicated_jobs: Optional[List[StrictStr]] = Field(default=None, description="TargetReplicatedJobs are the names of the replicated jobs the operator applies to. An empty list will apply to all replicatedJobs.", alias="targetReplicatedJobs")
    __properties: ClassVar[List[str]] = ["action", "name", "onJobFailureReasons", "targetReplicatedJobs"]

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
        """Create an instance of JobsetV1alpha2FailurePolicyRule from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobsetV1alpha2FailurePolicyRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action") if obj.get("action") is not None else '',
            "name": obj.get("name") if obj.get("name") is not None else '',
            "onJobFailureReasons": obj.get("onJobFailureReasons"),
            "targetReplicatedJobs": obj.get("targetReplicatedJobs")
        })
        return _obj


