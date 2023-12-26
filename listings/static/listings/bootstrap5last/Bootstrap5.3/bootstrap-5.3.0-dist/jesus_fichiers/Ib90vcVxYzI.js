;/*FB_PKG_DELIM*/

__d("BdPdcSignalsFalcoEvent",["FalcoLoggerInternal","getFalcoLogPolicy_DO_NOT_USE"],(function(a,b,c,d,e,f,g){"use strict";a=c("getFalcoLogPolicy_DO_NOT_USE")("1743095");b=d("FalcoLoggerInternal").create("bd_pdc_signals",a);e=b;g["default"]=e}),98);
__d("BotDetection_SignalFlags",[],(function(a,b,c,d,e,f){a=Object.freeze({ACTIVE:1,DYNAMIC:2,BIOMETRIC:4,DEPRECATED:8,WEB:16,IOS_NATIVE:32,ANDROID_NATIVE:64,EQUAL_BY_VALUE:128,EQUAL_BY_CONTEXT:256,EQUAL_BY_TIMESTAMP:512,SUSPICIOUS_TIER:1024,PARANOID_TIER:2048,RANDOM_SAMPLE_TIER_DEPRECATED:4096,BENIGN_TIER:262144,EMPLOYEES_TIER:524288,BUNDLE:8192,ONSITE:16384,OFFSITE:32768,OFFSITE_SENSITIVE:65536,SENSITIVE:131072});f["default"]=a}),66);
__d("BDOperationTypedLogger",["Banzai","GeneratedLoggerUtils"],(function(a,b,c,d,e,f){"use strict";a=function(){function a(){this.$1={}}var c=a.prototype;c.log=function(a){b("GeneratedLoggerUtils").log("logger:BDOperationLoggerConfig",this.$1,b("Banzai").BASIC,a)};c.logVital=function(a){b("GeneratedLoggerUtils").log("logger:BDOperationLoggerConfig",this.$1,b("Banzai").VITAL,a)};c.logImmediately=function(a){b("GeneratedLoggerUtils").log("logger:BDOperationLoggerConfig",this.$1,{signal:!0},a)};c.clear=function(){this.$1={};return this};c.getData=function(){return babelHelpers["extends"]({},this.$1)};c.updateData=function(a){this.$1=babelHelpers["extends"]({},this.$1,a);return this};c.setBdSessionID=function(a){this.$1.bd_session_id=a;return this};c.setComponent=function(a){this.$1.component=a;return this};c.setDurationUs=function(a){this.$1.duration_us=a;return this};c.setExceptionMessage=function(a){this.$1.exception_message=a;return this};c.setExceptionStackTrace=function(a){this.$1.exception_stack_trace=a;return this};c.setExceptionType=function(a){this.$1.exception_type=a;return this};c.setIntValue=function(a){this.$1.int_value=a;return this};c.setLevel=function(a){this.$1.level=a;return this};c.setOperation=function(a){this.$1.operation=a;return this};c.setOperationInfo=function(a){this.$1.operation_info=b("GeneratedLoggerUtils").serializeMap(a);return this};c.setSessionlets=function(a){this.$1.sessionlets=b("GeneratedLoggerUtils").serializeVector(a);return this};return a}();c={bd_session_id:!0,component:!0,duration_us:!0,exception_message:!0,exception_stack_trace:!0,exception_type:!0,int_value:!0,level:!0,operation:!0,operation_info:!0,sessionlets:!0};f["default"]=a}),66);
__d("BDSignalBufferData",[],(function(a,b,c,d,e,f){"use strict";a={};b=a;f["default"]=b}),66);
__d("BDSignalWrapper",["BDSignalBufferData","SignalCollectorMap"],(function(a,b,c,d,e,f,g){"use strict";a=function(){function a(a,b){this.signalFlags=a,this.signalType=b}var b=a.prototype;b.getSignalCollector=function(){return c("SignalCollectorMap").get(this.signalType)};b.getBufferConfig=function(){return c("BDSignalBufferData")[this.signalType]};return a}();g["default"]=a}),98);
__d("SignalValueContext",[],(function(a,b,c,d,e,f){"use strict";a=function(){function a(a){this.cn=a}var b=a.prototype;b.getSignalValueContextName=function(){return this.cn};return a}();f["default"]=a}),66);
__d("BDSignalCollectorBase",["BDSignalBufferData","SignalValueContext","regeneratorRuntime"],(function(a,b,c,d,e,f,g){"use strict";a=function(){function a(a){this.signalType=a}var d=a.prototype;d.executeSignalCollection=function(){throw new Error("Child class responsibility to implement executeSignalCollection")};d.executeAsyncSignalCollection=function(){var a;return b("regeneratorRuntime").async(function(c){while(1)switch(c.prev=c.next){case 0:c.next=2;return b("regeneratorRuntime").awrap(this.executeSignalCollection());case 2:a=c.sent;return c.abrupt("return",a);case 4:case"end":return c.stop()}},null,this)};a.getSanitizedURI=function(){var a=window.location.href,b=a.indexOf("?");return b<0?a:a.substring(0,b)};d.getContext=function(){return new(c("SignalValueContext"))(a.getSanitizedURI())};d.throwIfNotInitialized=function(){if(!(this.signalType in c("BDSignalBufferData")))throw new Error("Signal is not intialized")};return a}();g["default"]=a}),98);
__d("BDLoggingConstants",[],(function(a,b,c,d,e,f){"use strict";a={ERROR:"error",WARNING:"warning",