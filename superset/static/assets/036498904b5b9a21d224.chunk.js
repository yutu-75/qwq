"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[39502,39541],{109433:(e,t,a)=>{a.d(t,{CronPicker:()=>u});var l=a(205872),n=a.n(l),r=(a(667294),a(120271)),o=a(455867),i=a(751995),s=a(361247),c=a(211965);const d={everyText:(0,o.t)("every"),emptyMonths:(0,o.t)("every month"),emptyMonthDays:(0,o.t)("every day of the month"),emptyMonthDaysShort:(0,o.t)("day of the month"),emptyWeekDays:(0,o.t)("every day of the week"),emptyWeekDaysShort:(0,o.t)("day of the week"),emptyHours:(0,o.t)("every hour"),emptyMinutes:(0,o.t)("every minute"),emptyMinutesForHourPeriod:(0,o.t)("every"),yearOption:(0,o.t)("year"),monthOption:(0,o.t)("month"),weekOption:(0,o.t)("week"),dayOption:(0,o.t)("day"),hourOption:(0,o.t)("hour"),minuteOption:(0,o.t)("minute"),rebootOption:(0,o.t)("reboot"),prefixPeriod:(0,o.t)("Every"),prefixMonths:(0,o.t)("in"),prefixMonthDays:(0,o.t)("on"),prefixWeekDays:(0,o.t)("on"),prefixWeekDaysForMonthAndYearPeriod:(0,o.t)("and"),prefixHours:(0,o.t)("at"),prefixMinutes:(0,o.t)(":"),prefixMinutesForHourPeriod:(0,o.t)("at"),suffixMinutesForHourPeriod:(0,o.t)("minute(s)"),errorInvalidCron:(0,o.t)("Invalid cron expression"),clearButtonText:(0,o.t)("Clear"),weekDays:[(0,o.t)("Sunday"),(0,o.t)("Monday"),(0,o.t)("Tuesday"),(0,o.t)("Wednesday"),(0,o.t)("Thursday"),(0,o.t)("Friday"),(0,o.t)("Saturday")],months:[(0,o.t)("January"),(0,o.t)("February"),(0,o.t)("March"),(0,o.t)("April"),(0,o.t)("May"),(0,o.t)("June"),(0,o.t)("July"),(0,o.t)("August"),(0,o.t)("September"),(0,o.t)("October"),(0,o.t)("November"),(0,o.t)("December")],altWeekDays:[(0,o.t)("SUN"),(0,o.t)("MON"),(0,o.t)("TUE"),(0,o.t)("WED"),(0,o.t)("THU"),(0,o.t)("FRI"),(0,o.t)("SAT")],altMonths:[(0,o.t)("JAN"),(0,o.t)("FEB"),(0,o.t)("MAR"),(0,o.t)("APR"),(0,o.t)("MAY"),(0,o.t)("JUN"),(0,o.t)("JUL"),(0,o.t)("AUG"),(0,o.t)("SEP"),(0,o.t)("OCT"),(0,o.t)("NOV"),(0,o.t)("DEC")]},u=(0,i.iK)((e=>(0,c.tZ)(r.ZP,{getPopupContainer:e=>e.parentElement},(0,c.tZ)(s.default,n()({locale:d},e)))))`
  .react-js-cron-field {
    margin-bottom: 0px;
  }
  .react-js-cron-select:not(.react-js-cron-custom-select) > div:first-of-type,
  .react-js-cron-custom-select {
    border-radius: ${({theme:e})=>e.gridUnit}px;
    background-color: ${({theme:e})=>e.colors.grayscale.light4} !important;
  }
  .react-js-cron-custom-select > div:first-of-type {
    border-radius: ${({theme:e})=>e.gridUnit}px;
  }
  .react-js-cron-custom-select .ant-select-selection-placeholder {
    flex: auto;
  }
  .react-js-cron-custom-select .ant-select-selection-overflow-item {
    align-self: center;
  }
`},129848:(e,t,a)=>{a.d(t,{Z:()=>c});a(667294);var l=a(751995),n=a(358593),r=a(731293),o=a(211965);const i=l.iK.span`
  white-space: nowrap;
  min-width: 100px;
  svg,
  i {
    margin-right: 8px;

    &:hover {
      path {
        fill: ${({theme:e})=>e.colors.primary.base};
      }
    }
  }
`,s=l.iK.span`
  color: ${({theme:e})=>e.colors.grayscale.base};
`;function c({actions:e}){return(0,o.tZ)(i,{className:"actions"},e.map(((e,t)=>{const a=r.Z[e.icon];return e.tooltip?(0,o.tZ)(n.u,{id:`${e.label}-tooltip`,title:e.tooltip,placement:e.placement,key:t},(0,o.tZ)(s,{role:"button",tabIndex:0,className:"action-button","data-test":e.label,onClick:e.onClick},(0,o.tZ)(a,null))):(0,o.tZ)(s,{role:"button",tabIndex:0,className:"action-button",onClick:e.onClick,"data-test":e.label,key:t},(0,o.tZ)(a,null))})))}},888154:(e,t,a)=>{a.d(t,{Z:()=>s});var l=a(205872),n=a.n(l),r=a(667294),o=a(970553),i=a(211965);const s=({onChange:e,treeData:t=[],allowNewOptions:a,...l})=>{const[s,c]=(0,r.useState)(""),[d,u]=(0,r.useState)([]),[p,h]=(0,r.useState)([]),m=(e,t)=>{const a=e.indexOf(t),l=e.substr(0,a),n=e.substr(a+t.length);return a>-1?(0,i.tZ)("span",{"test-data":e,style:{color:"#000"}},l,(0,i.tZ)("span",{style:{color:"#f50"}},t),n):(0,i.tZ)("span",{"test-data":e,style:{color:"#000"}},e)},v=(e=[],t,a=!1)=>{if(!e||!t)return e;const l=[];return e.forEach((e=>{e.title.includes(t)?l.push({...e,title:m(e.title,t),children:v(e.children,t,!0)}):e.children&&e.children.length>0?a?(e.children=v(e.children,t,a),l.push({...e,title:m(e.title,t)})):(e.children=v(e.children,t),e.children.length>0&&l.push({...e,title:m(e.title,t)})):a&&l.push({...e,title:m(e.title,t)})})),l},g=(0,r.useMemo)((()=>{if(a){if(s){const e=v(JSON.parse(JSON.stringify(p)),s);return e.length?e:(h([{title:s,value:s},...t]),[{title:s,value:s}])}return"string"===typeof l.value?[{title:l.value,value:l.value},...t]:p}return v(JSON.parse(JSON.stringify(p)),s)}),[s,p]);return(0,r.useEffect)((()=>{"number"===typeof l.value&&h(t)}),[l.value]),(0,r.useEffect)((()=>{if(s){const e=v(JSON.parse(JSON.stringify(t)),s),a=e=>{let t=[];return e.forEach((e=>{t.push(e.value),e.children&&(t=t.concat(a(e.children)))})),t},l=a(e);u(l)}else u([])}),[t,s]),(0,r.useEffect)((()=>{h(t)}),[t]),(0,i.tZ)(o.Z,n()({filterTreeNode:()=>!0,treeExpandedKeys:d,onChange:t=>{c(""),e&&(l.labelInValue?e({...t,label:"string"===typeof t.label?t.label:t.label.props["test-data"]}):e(t))},treeData:g,onTreeExpand:e=>u(e),onSearch:e=>c(e)},l))}},112441:(e,t,a)=>{a.d(t,{r:()=>i});a(667294);var l=a(751995),n=a(840987),r=a(211965);const o=(0,l.iK)(n.Z)`
  .ant-switch-checked {
    background-color: ${({theme:e})=>e.colors.primary.base};
  }
`,i=e=>(0,r.tZ)(o,e)},898978:(e,t,a)=>{a.d(t,{Z:()=>y});var l=a(211965),n=a(667294),r=a(480008),o=a.n(r),i=a(455867),s=a(49937);const c="GMT Standard Time",d="Africa/Abidjan",u="400px",p={"-300-240":["Eastern Standard Time","Eastern Daylight Time"],"-360-300":["Central Standard Time","Central Daylight Time"],"-420-360":["Mountain Standard Time","Mountain Daylight Time"],"-420-420":["Mountain Standard Time - Phoenix","Mountain Standard Time - Phoenix"],"-480-420":["Pacific Standard Time","Pacific Daylight Time"],"-540-480":["Alaska Standard Time","Alaska Daylight Time"],"-600-600":["Hawaii Standard Time","Hawaii Daylight Time"],60120:["Central European Time","Central European Daylight Time"],"00":[c,c],"060":["GMT Standard Time - London","British Summer Time"]},h=o()(),m=o()([2021,1]),v=o()([2021,7]),g=e=>m.tz(e).utcOffset().toString()+v.tz(e).utcOffset().toString(),T=e=>{var t,a;const l=g(e);return(h.tz(e).isDST()?null==(t=p[l])?void 0:t[1]:null==(a=p[l])?void 0:a[0])||e},b=o().tz.countries().map((e=>o().tz.zonesForCountry(e,!0))).flat(),E=[];b.forEach((e=>{E.find((t=>g(t.name)===g(e.name)))||E.push(e)}));const _=E.map((e=>({label:`GMT ${o().tz(h,e.name).format("Z")} (${T(e.name)})`,value:e.name,offsets:g(e.name),timezoneName:e.name}))),Z=(e,t)=>o().tz(h,e.timezoneName).utcOffset()-o().tz(h,t.timezoneName).utcOffset();_.sort(Z);const f=e=>{var t;return(null==(t=_.find((t=>t.offsets===g(e))))?void 0:t.value)||d};function y({onTimezoneChange:e,timezone:t,minWidth:a=u}){const r=(0,n.useMemo)((()=>f(t||o().tz.guess())),[t]);return(0,n.useEffect)((()=>{t!==r&&e(r)}),[r,e,t]),(0,l.tZ)(s.Ph,{ariaLabel:(0,i.t)("Timezone selector"),css:(0,l.iv)({minWidth:a},"",""),onChange:t=>e(t),value:r,options:_,sortComparator:Z})}},363082:(e,t,a)=>{a.r(t),a.d(t,{default:()=>xe});var l=a(667294),n=a(616550),r=a(175049),o=a(455867),i=a(522102),s=a(751995),c=a(431069),d=a(730381),u=a.n(d),p=a(129848),h=a(222545),m=a(358593),v=a(418782),g=a(620755),T=a(427600),b=a(414114),E=a(246714),_=a(211965),Z=a(731293),f=a(802849);const y=e=>_.iv`
  color: ${e.colors.grayscale.light1};
  margin-right: ${2*e.gridUnit}px;
`;function N({type:e}){const t={icon:null,label:""};switch(e){case f.u.Email:t.icon=(0,_.tZ)(Z.Z.Email,{css:y}),t.label=f.u.Email;break;case f.u.Slack:t.icon=(0,_.tZ)(Z.Z.Slack,{css:y}),t.label=f.u.Slack;break;default:t.icon=null,t.label=""}return t.icon?(0,_.tZ)(m.u,{title:t.label,placement:"bottom"},t.icon):null}var S=a(419259),x=a(217198);u().updateLocale("en",{calendar:{lastDay:"[Yesterday at] LTS",sameDay:"[Today at] LTS",nextDay:"[Tomorrow at] LTS",lastWeek:"[last] dddd [at] LTS",nextWeek:"dddd [at] LTS",sameElse:"L"}});const C=s.iK.span`
  color: ${({theme:e})=>e.colors.grayscale.base};
`,A=(0,s.iK)(Z.Z.Refresh)`
  color: ${({theme:e})=>e.colors.primary.base};
  width: auto;
  height: ${({theme:e})=>5*e.gridUnit}px;
  position: relative;
  top: ${({theme:e})=>e.gridUnit}px;
  left: ${({theme:e})=>e.gridUnit}px;
  cursor: pointer;
`,D=({updatedAt:e,update:t})=>{const[a,n]=(0,l.useState)(u()(e));return(0,l.useEffect)((()=>{n((()=>u()(e)));const t=setInterval((()=>{n((()=>u()(e)))}),6e4);return()=>clearInterval(t)}),[e]),(0,_.tZ)(C,null,(0,o.t)("Last Updated %s",a.isValid()?a.calendar():"--"),t&&(0,_.tZ)(A,{onClick:t}))};var O=a(34858),k=a(440768),R=a(653002),w=a(115926),I=a.n(w),X=a(112441),$=a(774069),L=a(898978),M=a(287183),U=a(985633),H=a(591877),P=a(593185),z=a(49937),j=a(542878),G=a(301483),q=a(409882),W=a(9875),F=a(109433);const V=({value:e,onChange:t})=>{const a=(0,s.Fg)(),n=(0,l.useRef)(null),[r,i]=(0,l.useState)("picker"),c=(0,l.useCallback)((e=>i(e.target.value)),[]),d=(0,l.useCallback)((e=>{var a;t(e),null==(a=n.current)||a.setValue(e)}),[n,t]),u=(0,l.useCallback)((e=>{t(e.target.value)}),[t]),p=(0,l.useCallback)((()=>{var e;t((null==(e=n.current)?void 0:e.input.value)||"")}),[t]),[h,m]=(0,l.useState)();return(0,_.tZ)(l.Fragment,null,(0,_.tZ)(M.Y.Group,{onChange:c,value:r},(0,_.tZ)("div",{className:"inline-container add-margin"},(0,_.tZ)(M.Y,{"data-test":"picker",value:"picker"}),(0,_.tZ)(F.CronPicker,{clearButton:!1,value:e,setValue:d,disabled:"picker"!==r,displayError:"picker"===r,onError:m})),(0,_.tZ)("div",{className:"inline-container add-margin"},(0,_.tZ)(M.Y,{"data-test":"input",value:"input"}),(0,_.tZ)("span",{className:"input-label"},(0,o.t)("CRON Schedule")),(0,_.tZ)(de,{"data-test":"input-content",className:"styled-input"},(0,_.tZ)("div",{className:"input-container"},(0,_.tZ)(W.II,{type:"text",name:"crontab",ref:n,style:h?{borderColor:a.colors.error.base}:{},placeholder:(0,o.t)("CRON expression"),disabled:"input"!==r,onBlur:u,onPressEnter:p}))))))},B=s.iK.div`
  margin-bottom: 10px;

  .input-container {
    textarea {
      height: auto;
    }
  }

  .inline-container {
    margin-bottom: 10px;

    .input-container {
      margin-left: 10px;
    }

    > div {
      margin: 0;
    }

    .delete-button {
      margin-left: 10px;
      padding-top: 3px;
    }
  }
`,K=({setting:e=null,index:t,onUpdate:a,onRemove:n})=>{const{method:r,recipients:i}=e||{},[c,d]=(0,l.useState)(i||""),u=(0,s.Fg)();if(!e)return null;i&&c!==i&&d(i);const p={Email:(0,o.t)("Recipient email")+";"+(0,o.t)("For example")+":202212111@any3.com\u3001xxx@any3.com(any3"+(0,o.t)("Case insensitive")+");",IChangAn:(0,o.t)("Recipient account")+"("+(0,o.t)("Job ID")+");"+(0,o.t)("For example")+": 202212111\u3001xxx;",Wecom:(0,o.t)("Recipient account")+"("+(0,o.t)("Job ID")+");"+(0,o.t)("For example")+": 202212111\u3001xxx;"};return(0,_.tZ)(B,null,(0,_.tZ)("div",{className:"inline-container"},(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"input-container"},(0,_.tZ)(z.Ph,{ariaLabel:(0,o.t)("Delivery method"),"data-test":"select-delivery-method",onChange:l=>{if(d(""),a){const n={...e,method:l,recipients:""};a(t,n)}},placeholder:(0,o.t)("Select Delivery Method"),options:[{value:"Email",label:(0,o.t)("Email")},{value:"IChangAn",label:(0,o.t)("IChangAn")},{value:"Wecom",label:(0,o.t)("Wecom")}],value:r}))),void 0!==r&&n?(0,_.tZ)("span",{role:"button",tabIndex:0,className:"delete-button",onClick:()=>n(t)},(0,_.tZ)(Z.Z.Trash,{iconColor:u.colors.grayscale.base})):null),void 0!==r?(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"control-label"},(0,o.t)(r)),(0,_.tZ)("div",{className:"input-container"},(0,_.tZ)("textarea",{name:"recipients",value:c,onChange:l=>{const{target:n}=l;if(d(n.value),a){const l={...e,recipients:n.value};a(t,l)}},placeholder:p[r]})),(0,_.tZ)("div",{className:"helper"},(0,o.t)('Recipients are separated by "," or ";"'))):null)};var J=a(888154);const Y=["pivot_table","pivot_table_v2","table","paired_ttest"],Q=["Email"],ee="PNG",te=[{label:(0,o.t)("< (Smaller than)"),value:"<"},{label:(0,o.t)("> (Larger than)"),value:">"},{label:(0,o.t)("<= (Smaller or equal)"),value:"<="},{label:(0,o.t)(">= (Larger or equal)"),value:">="},{label:(0,o.t)("== (Is equal)"),value:"=="},{label:(0,o.t)("!= (Is not equal)"),value:"!="},{label:(0,o.t)("Not null"),value:"not null"}],ae=[{label:(0,o.t)("None"),value:0},{label:(0,o.t)("30 days"),value:30},{label:(0,o.t)("60 days"),value:60},{label:(0,o.t)("90 days"),value:90}],le="0 * * * *",ne={active:!0,creation_method:"alerts_reports",crontab:le,log_retention:90,working_timeout:3600,name:"",owners:[],recipients:[],sql:"",validator_config_json:{},validator_type:"",force_screenshot:!1,grace_period:void 0},re=(0,s.iK)($.Z)`
  max-width: 1200px;
  width: 100%;

  .ant-modal-body {
    overflow: initial;
  }
`,oe=e=>_.iv`
  margin: auto ${2*e.gridUnit}px auto 0;
  color: ${e.colors.grayscale.base};
`,ie=s.iK.div`
  display: flex;
  flex-direction: column;

  .control-label {
    margin-top: ${({theme:e})=>e.gridUnit}px;
  }

  .header-section {
    display: flex;
    flex: 0 0 auto;
    align-items: center;
    width: 100%;
    padding: ${({theme:e})=>4*e.gridUnit}px;
    border-bottom: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
  }

  .column-section {
    display: flex;
    flex: 1 1 auto;

    .column {
      flex: 1 1 auto;
      min-width: calc(33.33% - ${({theme:e})=>8*e.gridUnit}px);
      padding: ${({theme:e})=>4*e.gridUnit}px;

      .async-select {
        margin: 10px 0 20px;
      }

      &.condition {
        border-right: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
      }

      &.message {
        border-left: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
      }
    }
  }

  .inline-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    &.wrap {
      flex-wrap: wrap;
    }

    > div {
      flex: 1 1 auto;
    }

    &.add-margin {
      margin-bottom: 5px;
    }

    .styled-input {
      margin: 0 0 0 10px;

      input {
        flex: 0 0 auto;
      }
    }
  }
`,se=s.iK.div`
  display: flex;
  align-items: center;
  margin: ${({theme:e})=>2*e.gridUnit}px auto
    ${({theme:e})=>4*e.gridUnit}px auto;

  h4 {
    margin: 0;
  }

  .required {
    margin-left: ${({theme:e})=>e.gridUnit}px;
    color: ${({theme:e})=>e.colors.error.base};
  }
`,ce=s.iK.div`
  display: flex;
  align-items: center;
  margin-top: 10px;

  .switch-label {
    margin-left: 10px;
  }
`,de=s.iK.div`
  flex: 1;
  margin-top: 0;

  .helper {
    display: block;
    color: ${({theme:e})=>e.colors.grayscale.base};
    font-size: ${({theme:e})=>e.typography.sizes.s}px;
    padding: ${({theme:e})=>e.gridUnit}px 0;
    text-align: left;
  }

  .required {
    margin-left: ${({theme:e})=>e.gridUnit/2}px;
    color: ${({theme:e})=>e.colors.error.base};
  }

  .input-container {
    display: flex;
    align-items: center;

    > div {
      width: 100%;
    }

    label {
      display: flex;
      margin-right: ${({theme:e})=>2*e.gridUnit}px;
    }

    i {
      margin: 0 ${({theme:e})=>e.gridUnit}px;
    }
  }

  input,
  textarea {
    flex: 1 1 auto;
  }

  input[disabled] {
    color: ${({theme:e})=>e.colors.grayscale.base};
  }

  textarea {
    height: 300px;
    resize: none;
  }

  input::placeholder,
  textarea::placeholder {
    color: ${({theme:e})=>e.colors.grayscale.light1};
  }

  textarea,
  input[type='text'],
  input[type='number'] {
    padding: ${({theme:e})=>e.gridUnit}px
      ${({theme:e})=>2*e.gridUnit}px;
    border-style: none;
    border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    border-radius: ${({theme:e})=>e.gridUnit}px;

    &[name='description'] {
      flex: 1 1 auto;
    }
  }

  .input-label {
    margin-left: 10px;
  }
`,ue=(0,s.iK)(M.Y)`
  display: block;
  line-height: ${({theme:e})=>7*e.gridUnit}px;
`,pe=(0,s.iK)(M.Y.Group)`
  margin-left: ${({theme:e})=>5.5*e.gridUnit}px;
`,he=(0,s.iK)(z.r4)`
  margin-left: ${({theme:e})=>5.5*e.gridUnit}px;
  margin-top: ${({theme:e})=>e.gridUnit}px;
`,me=s.iK.div`
  color: ${({theme:e})=>e.colors.primary.dark1};
  cursor: pointer;

  i {
    margin-right: ${({theme:e})=>2*e.gridUnit}px;
  }

  &.disabled {
    color: ${({theme:e})=>e.colors.grayscale.light1};
    cursor: default;
  }
`,ve=s.iK.div`
  .inline-container .input-container {
    margin-left: 0;
  }
`,ge=e=>_.iv`
    margin-right: ${3*e.gridUnit}px;
  `,Te={ADD_NOTIFICATION_METHOD_TEXT:(0,o.t)("Add notification method"),ADD_DELIVERY_METHOD_TEXT:(0,o.t)("Add delivery method"),SAVE_TEXT:(0,o.t)("Save"),ADD_TEXT:(0,o.t)("Add"),EDIT_REPORT_TEXT:(0,o.t)("Edit Report"),EDIT_ALERT_TEXT:(0,o.t)("Edit Alert"),ADD_REPORT_TEXT:(0,o.t)("Add Report"),ADD_ALERT_TEXT:(0,o.t)("Add Alert"),REPORT_NAME_TEXT:(0,o.t)("Report name"),ALERT_NAME_TEXT:(0,o.t)("Alert name"),OWNERS_TEXT:(0,o.t)("Owners"),DESCRIPTION_TEXT:(0,o.t)("Description"),ACTIVE_TEXT:(0,o.t)("Active"),ALERT_CONDITION_TEXT:(0,o.t)("Alert condition"),DATABASE_TEXT:(0,o.t)("Database"),SQL_QUERY_TEXT:(0,o.t)("SQL Query"),TRIGGER_ALERT_IF_TEXT:(0,o.t)("Trigger Alert If..."),CONDITION_TEXT:(0,o.t)("Condition"),VALUE_TEXT:(0,o.t)("Value"),VALUE_TOOLTIP:(0,o.t)("Threshold value should be double precision number"),REPORT_SCHEDULE_TEXT:(0,o.t)("Report schedule"),ALERT_CONDITION_SCHEDULE_TEXT:(0,o.t)("Alert condition schedule"),TIMEZONE_TEXT:(0,o.t)("Timezone"),SCHEDULE_SETTINGS_TEXT:(0,o.t)("Schedule settings"),LOG_RETENTION_TEXT:(0,o.t)("Log retention"),WORKING_TIMEOUT_TEXT:(0,o.t)("Working timeout"),TIME_IN_SECONDS_TEXT:(0,o.t)("Time in seconds"),SECONDS_TEXT:(0,o.t)("seconds"),GRACE_PERIOD_TEXT:(0,o.t)("Grace period"),MESSAGE_CONTENT_TEXT:(0,o.t)("Message content"),DASHBOARD_TEXT:(0,o.t)("Dashboard"),CHART_TEXT:(0,o.t)("Chart"),SEND_AS_PNG_TEXT:(0,o.t)("Send as PNG"),SEND_AS_CSV_TEXT:(0,o.t)("Send as CSV"),SEND_AS_TEXT:(0,o.t)("Send as text"),IGNORE_CACHE_TEXT:(0,o.t)("Ignore cache when generating screenshot"),NOTIFICATION_METHOD_TEXT:(0,o.t)("Notification method")},be=({status:e="active",onClick:t})=>{if("hidden"===e)return null;return(0,_.tZ)(me,{className:e,onClick:()=>{"disabled"!==e&&t()}},(0,_.tZ)("i",{className:"fa fa-plus"})," ","active"===e?Te.ADD_NOTIFICATION_METHOD_TEXT:Te.ADD_DELIVERY_METHOD_TEXT)},Ee=(0,b.ZP)((({addDangerToast:e,onAdd:t,onHide:a,show:n,alert:r=null,isReport:i=!1,addSuccessToast:s})=>{var d,u,p,h,m,v,g,T,b,E,f,y,N,S,x,C;const A=(0,G.c)(),D=(null==A?void 0:A.ALERT_REPORTS_NOTIFICATION_METHODS)||Q,[k,R]=(0,l.useState)(!0),[w,$]=(0,l.useState)(),[W,F]=(0,l.useState)(!0),[B,me]=(0,l.useState)("dashboard"),[Ee,_e]=(0,l.useState)(ee),[Ze,fe]=(0,l.useState)(!1),[ye,Ne]=(0,l.useState)(!1),[Se,xe]=(0,l.useState)([]),[Ce,Ae]=(0,l.useState)([]),[De,Oe]=(0,l.useState)([]),[ke,Re]=(0,l.useState)([]),[we,Ie]=(0,l.useState)([]),[Xe,$e]=(0,l.useState)(""),Le=null!==r,Me="chart"===B&&((0,H.cr)(P.T.ALERTS_ATTACH_REPORTS)||i),[Ue,He]=(0,l.useState)("active"),[Pe,ze]=(0,l.useState)([]),je=(e,t)=>{const a=Pe.slice();a[e]=t,ze(a),void 0!==t.method&&"hidden"!==Ue&&He("active")},Ge=e=>{const t=Pe.slice();t.splice(e,1),ze(t),He("active")},{state:{loading:qe,resource:We,error:Fe},fetchResource:Ve,createResource:Be,updateResource:Ke,clearError:Je}=(0,O.LE)("report",(0,o.t)("report"),e),Ye=()=>{Je(),F(!0),a(),ze([]),$({...ne}),He("active")},Qe=(0,l.useMemo)((()=>(e="",t,a)=>{const l=I().encode({filter:e,page:t,page_size:a});return c.Z.get({endpoint:`/api/v1/report/related/created_by?q=${l}`}).then((e=>({data:e.json.result.map((e=>({value:e.value,label:e.text}))),totalCount:e.json.count})))}),[]),et=(0,l.useCallback)((e=>{const t=e||(null==w?void 0:w.database);if(!t||t.label)return null;let a;return Se.forEach((e=>{e.value!==t.value&&e.value!==t.id||(a=e)})),a}),[null==w?void 0:w.database,Se]),tt=(e,t)=>{$((a=>({...a,[e]:t})))},at=(0,l.useMemo)((()=>(e="",t,a)=>{const l=I().encode({filter:e,page:t,page_size:a});return c.Z.get({endpoint:`/api/v1/report/related/database?q=${l}`}).then((e=>{const t=e.json.result.map((e=>({value:e.value,label:e.text})));return xe(t),{data:t,totalCount:e.json.count}}))}),[]),lt=(null==w?void 0:w.database)&&!w.database.label;(0,l.useEffect)((()=>{lt&&tt("database",et())}),[lt,et]),(0,l.useEffect)((()=>{c.Z.get({endpoint:"/api/v2/dashboard/group/"}).then((e=>{const{json:{meta:{code:t,data:a=[]}}}=e;if(200==t&&Array.isArray(a)){const e=t=>t.map((t=>({title:t.name,value:t.group_id,selectable:!1,children:[...e(t.children),...t.dashboards.map((e=>({title:e.dashboard_title,value:e.dashboard_id})))]}))),t=e(JSON.parse(JSON.stringify(a)));Re(t)}}))}),[]),(0,l.useEffect)((()=>{c.Z.get({endpoint:"api/v2/chart/group/"}).then((e=>{const{json:{meta:{code:t,data:a=[]}}}=e;if(200==t&&Array.isArray(a)){const e=t=>t.map((t=>({title:t.name,value:t.group_id,selectable:!1,children:[...e(t.children),...t.slices.map((e=>({title:e.slice_name,value:e.slice_id})))]}))),t=e(a);Ie(t)}}))}),[]);const nt=(0,l.useMemo)((()=>(e="",t,a)=>{const l=I().encode_uri({filter:e,page:t,page_size:a});return c.Z.get({endpoint:`/api/v1/report/related/dashboard?q=${l}`}).then((e=>{const t=e.json.result.map((e=>({value:e.value,label:e.text})));return Ae(t),{data:t,totalCount:e.json.count}}))}),[]),rt=e=>{const t=e||(null==w?void 0:w.dashboard);if(!t||t.label)return null;let a;return Ce.forEach((e=>{e.value!==t.value&&e.value!==t.id||(a=e)})),a},ot=(0,l.useCallback)((e=>{const t=e||(null==w?void 0:w.chart);if(!t||t.label)return null;let a;return De.forEach((e=>{e.value!==t.value&&e.value!==t.id||(a=e)})),a}),[De,null==w?void 0:w.chart]),it=(null==w?void 0:w.chart)&&!(null!=w&&w.chart.label);(0,l.useEffect)((()=>{it&&tt("chart",ot())}),[ot,it]);const st=(0,l.useMemo)((()=>(e="",t,a)=>{const l=I().encode_uri({filter:e,page:t,page_size:a});return c.Z.get({endpoint:`/api/v1/report/related/chart?q=${l}`}).then((e=>{const t=e.json.result.map((e=>({value:e.value,label:e.text})));return Oe(t),{data:t,totalCount:e.json.count}}))}),[]),ct=e=>{const{target:t}=e;tt(t.name,t.value)},dt=e=>{const{target:t}=e,a=+t.value;tt(t.name,0===a?null:a?Math.max(a,1):a)},ut=e=>{tt("dashboard",e||void 0),tt("chart",null)},pt=e=>{(e=>{c.Z.get({endpoint:`/api/v1/chart/${e.value}`}).then((e=>$e(e.json.result.viz_type)))})(e),tt("chart",e||void 0),tt("dashboard",null)},ht=()=>{var e,t,a,l,n,r;null!=w&&null!=(e=w.name)&&e.length&&null!=w&&null!=(t=w.owners)&&t.length&&null!=w&&null!=(a=w.crontab)&&a.length&&void 0!==(null==w?void 0:w.working_timeout)&&("dashboard"===B&&null!=w&&w.dashboard||"chart"===B&&null!=w&&w.chart)&&(()=>{if(!Pe.length)return!1;let e=!1;return Pe.forEach((t=>{var a;t.method&&null!=(a=t.recipients)&&a.length&&(e=!0)})),e})()?i||w.database&&null!=(l=w.sql)&&l.length&&(ye||null!=(n=w.validator_config_json)&&n.op)&&(ye||void 0!==(null==(r=w.validator_config_json)?void 0:r.threshold))?R(!1):R(!0):R(!0)};(0,l.useEffect)((()=>{if(Le&&(null==w||!w.id||(null==r?void 0:r.id)!==w.id||W&&n)){if(null!==(null==r?void 0:r.id)&&!qe&&!Fe){const e=r.id||0;Ve(e)}}else!Le&&(!w||w.id||W&&n)&&($({...ne}),ze([]),He("active"))}),[r]),(0,l.useEffect)((()=>{if(We){const e=(We.recipients||[]).map((e=>{const t="string"===typeof e.recipient_config_json?JSON.parse(e.recipient_config_json):{};return{method:e.type,recipients:t.target||e.recipient_config_json,options:D}}));ze(e),He(e.length===D.length?"hidden":"active"),me(We.chart?"chart":"dashboard"),_e(We.chart&&We.report_format||ee);const t="string"===typeof We.validator_config_json?JSON.parse(We.validator_config_json):We.validator_config_json;Ne("not null"===We.validator_type),We.chart&&$e(We.chart.viz_type),fe(We.force_screenshot),$({...We,chart:We.chart?ot(We.chart)||{value:We.chart.id,label:We.chart.slice_name}:void 0,dashboard:We.dashboard?rt(We.dashboard)||{value:We.dashboard.id,label:We.dashboard.dashboard_title}:void 0,database:We.database?et(We.database)||{value:We.database.id,label:We.database.database_name}:void 0,owners:((null==r?void 0:r.owners)||[]).map((e=>({value:e.value||e.id,label:e.label||`${e.first_name} ${e.last_name}`}))),validator_config_json:"not null"===We.validator_type?{op:"not null"}:t})}}),[We]);const mt=w||{};return(0,l.useEffect)((()=>{ht()}),[mt.name,mt.owners,mt.database,mt.sql,mt.validator_config_json,mt.crontab,mt.working_timeout,mt.dashboard,mt.chart,B,Pe,ye]),W&&n&&F(!1),(0,_.tZ)(re,{className:"no-content-padding",responsive:!0,disablePrimaryButton:k,onHandledPrimaryAction:()=>{var e,a,l;const n=[];Pe.forEach((e=>{e.method&&e.recipients.length&&n.push({recipient_config_json:{target:e.recipients},type:e.method})}));const r="chart"===B&&!i,c={...w,type:i?(0,o.t)("Report"):(0,o.t)("Alert"),force_screenshot:r||Ze,validator_type:ye?"not null":"operator",validator_config_json:ye?{}:null==w?void 0:w.validator_config_json,chart:"chart"===B?null==w||null==(e=w.chart)?void 0:e.value:null,dashboard:"dashboard"===B?null==w||null==(a=w.dashboard)?void 0:a.value:null,database:null==w||null==(l=w.database)?void 0:l.value,owners:((null==w?void 0:w.owners)||[]).map((e=>e.value||e.id)),recipients:n,report_format:"dashboard"===B?ee:Ee||ee};if(c.recipients&&!c.recipients.length&&delete c.recipients,c.context_markdown="string",Le){if(null!=w&&w.id){const e=w.id;delete c.id,delete c.created_by,delete c.last_eval_dttm,delete c.last_state,delete c.last_value,delete c.last_value_row_json,Ke(e,c).then((e=>{e&&(s((0,o.t)("%s updated",c.type)),t&&t(),Ye())}))}}else w&&Be(c).then((e=>{e&&(s((0,o.t)("%s updated",c.type)),t&&t(e),Ye())}))},onHide:Ye,primaryButtonName:Le?Te.SAVE_TEXT:Te.ADD_TEXT,show:n,width:"100%",maxWidth:"1450px",title:(0,_.tZ)("h4",{"data-test":"alert-report-modal-title"},Le?(0,_.tZ)(Z.Z.EditAlt,{css:oe}):(0,_.tZ)(Z.Z.PlusLarge,{css:oe}),Le&&i?Te.EDIT_REPORT_TEXT:Le?Te.EDIT_ALERT_TEXT:i?Te.ADD_REPORT_TEXT:Te.ADD_ALERT_TEXT)},(0,_.tZ)(ie,null,(0,_.tZ)("div",{className:"header-section"},(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"control-label"},i?Te.REPORT_NAME_TEXT:Te.ALERT_NAME_TEXT,(0,_.tZ)("span",{className:"required"},"*")),(0,_.tZ)("div",{className:"input-container"},(0,_.tZ)("input",{type:"text",name:"name",value:w?w.name:"",placeholder:i?Te.REPORT_NAME_TEXT:Te.ALERT_NAME_TEXT,onChange:ct,css:ge}))),(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"control-label"},Te.OWNERS_TEXT,(0,_.tZ)("span",{className:"required"},"*")),(0,_.tZ)("div",{"data-test":"owners-select",className:"input-container"},(0,_.tZ)(z.qb,{ariaLabel:Te.OWNERS_TEXT,allowClear:!0,name:"owners",mode:"multiple",value:(null==w?void 0:w.owners)||[],options:Qe,onChange:e=>{tt("owners",e||[])},css:ge}))),(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"control-label"},Te.DESCRIPTION_TEXT),(0,_.tZ)("div",{className:"input-container"},(0,_.tZ)("input",{type:"text",name:"description",value:w&&w.description||"",placeholder:Te.DESCRIPTION_TEXT,onChange:ct,css:ge}))),(0,_.tZ)(ce,null,(0,_.tZ)(X.r,{onChange:e=>{tt("active",e)},checked:!w||w.active}),(0,_.tZ)("div",{className:"switch-label"},Te.ACTIVE_TEXT))),(0,_.tZ)("div",{className:"column-section"},!i&&(0,_.tZ)("div",{className:"column condition"},(0,_.tZ)(se,null,(0,_.tZ)("h4",null,Te.ALERT_CONDITION_TEXT)),(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"control-label"},Te.DATABASE_TEXT,(0,_.tZ)("span",{className:"required"},"*")),(0,_.tZ)("div",{className:"input-container"},(0,_.tZ)(z.qb,{ariaLabel:Te.DATABASE_TEXT,name:"source",value:null!=w&&null!=(d=w.database)&&d.label&&null!=w&&null!=(u=w.database)&&u.value?{value:w.database.value,label:w.database.label}:void 0,options:at,onChange:e=>{tt("database",e||[])}}))),(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"control-label"},Te.SQL_QUERY_TEXT,(0,_.tZ)("span",{className:"required"},"*")),(0,_.tZ)(j.Z,{name:"sql",language:"sql",offerEditInModal:!1,minLines:15,maxLines:15,onChange:e=>{tt("sql",e||"")},readOnly:!1,initialValue:null==We?void 0:We.sql,key:null==w?void 0:w.id})),(0,_.tZ)("div",{className:"inline-container wrap"},(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"control-label",css:ge},Te.TRIGGER_ALERT_IF_TEXT,(0,_.tZ)("span",{className:"required"},"*")),(0,_.tZ)("div",{className:"input-container"},(0,_.tZ)(z.Ph,{ariaLabel:Te.CONDITION_TEXT,onChange:e=>{var t;Ne("not null"===e);const a={op:e,threshold:w?null==(t=w.validator_config_json)?void 0:t.threshold:void 0};tt("validator_config_json",a)},placeholder:"Condition",value:(null==w||null==(p=w.validator_config_json)?void 0:p.op)||void 0,options:te,css:ge}))),(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"control-label"},Te.VALUE_TEXT," ",(0,_.tZ)(q.V,{tooltip:Te.VALUE_TOOLTIP}),(0,_.tZ)("span",{className:"required"},"*")),(0,_.tZ)("div",{className:"input-container"},(0,_.tZ)("input",{type:"number",name:"threshold",disabled:ye,value:void 0!==(null==w||null==(h=w.validator_config_json)?void 0:h.threshold)?w.validator_config_json.threshold:"",placeholder:Te.VALUE_TEXT,onChange:e=>{var t;const{target:a}=e,l={op:w?null==(t=w.validator_config_json)?void 0:t.op:void 0,threshold:a.value};tt("validator_config_json",l)}}))))),(0,_.tZ)("div",{className:"column schedule"},(0,_.tZ)(se,null,(0,_.tZ)("h4",null,i?Te.REPORT_SCHEDULE_TEXT:Te.ALERT_CONDITION_SCHEDULE_TEXT),(0,_.tZ)("span",{className:"required"},"*")),(0,_.tZ)(V,{value:(null==w?void 0:w.crontab)||le,onChange:e=>tt("crontab",e)}),(0,_.tZ)("div",{className:"control-label"},Te.TIMEZONE_TEXT),(0,_.tZ)("div",{className:"input-container",css:e=>(e=>_.iv`
  margin: ${3*e.gridUnit}px 0;
`)(e)},(0,_.tZ)(L.Z,{onTimezoneChange:e=>{tt("timezone",e)},timezone:null==w?void 0:w.timezone,minWidth:"100%"})),(0,_.tZ)(se,null,(0,_.tZ)("h4",null,Te.SCHEDULE_SETTINGS_TEXT)),(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"control-label"},Te.LOG_RETENTION_TEXT,(0,_.tZ)("span",{className:"required"},"*")),(0,_.tZ)("div",{className:"input-container"},(0,_.tZ)(z.Ph,{ariaLabel:Te.LOG_RETENTION_TEXT,placeholder:Te.LOG_RETENTION_TEXT,onChange:e=>{tt("log_retention",e)},value:"number"===typeof(null==w?void 0:w.log_retention)?null==w?void 0:w.log_retention:90,options:ae,sortComparator:(0,U.mj)("value")}))),(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"control-label"},Te.WORKING_TIMEOUT_TEXT,(0,_.tZ)("span",{className:"required"},"*")),(0,_.tZ)("div",{className:"input-container"},(0,_.tZ)("input",{type:"number",min:"1",name:"working_timeout",value:(null==w?void 0:w.working_timeout)||"",placeholder:Te.TIME_IN_SECONDS_TEXT,onChange:dt}),(0,_.tZ)("span",{className:"input-label"},Te.SECONDS_TEXT))),!i&&(0,_.tZ)(de,null,(0,_.tZ)("div",{className:"control-label"},Te.GRACE_PERIOD_TEXT),(0,_.tZ)("div",{className:"input-container"},(0,_.tZ)("input",{type:"number",min:"1",name:"grace_period",value:(null==w?void 0:w.grace_period)||"",placeholder:Te.TIME_IN_SECONDS_TEXT,onChange:dt}),(0,_.tZ)("span",{className:"input-label"},Te.SECONDS_TEXT)))),(0,_.tZ)("div",{className:"column message",style:{maxHeight:"calc(100vh - 246px)"}},(0,_.tZ)(se,null,(0,_.tZ)("h4",null,Te.MESSAGE_CONTENT_TEXT),(0,_.tZ)("span",{className:"required"},"*")),(0,_.tZ)(M.Y.Group,{onChange:e=>{const{target:t}=e;fe(!1),setTimeout((()=>me(t.value)),200)},value:B},(0,_.tZ)(ue,{value:"dashboard"},Te.DASHBOARD_TEXT),(0,_.tZ)(ue,{value:"chart"},Te.CHART_TEXT)),"chart"===B?we?(0,_.tZ)(J.Z,{ariaLabel:Te.CHART_TEXT,name:"chart",showSearch:!0,style:{width:"100%"},dropdownStyle:{maxHeight:400,overflow:"auto"},placeholder:(0,o.t)("search for"),value:null!=w&&null!=(m=w.chart)&&m.label&&null!=w&&null!=(v=w.chart)&&v.value?{value:w.chart.value,label:w.chart.label}:void 0,allowClear:!0,labelInValue:!0,onChange:pt,treeData:we||[]}):(0,_.tZ)(z.qb,{ariaLabel:Te.CHART_TEXT,name:"chart",value:null!=w&&null!=(g=w.chart)&&g.label&&null!=w&&null!=(T=w.chart)&&T.value?{value:null==w||null==(b=w.chart)?void 0:b.value,label:null==w||null==(E=w.chart)?void 0:E.label}:void 0,options:st||[],onChange:pt}):ke?(0,_.tZ)(J.Z,{ariaLabel:Te.DASHBOARD_TEXT,name:"dashboard",showSearch:!0,style:{width:"100%"},dropdownStyle:{maxHeight:400,overflow:"auto"},placeholder:(0,o.t)("search for"),value:null!=w&&null!=(f=w.dashboard)&&f.label&&null!=w&&null!=(y=w.dashboard)&&y.value?{value:w.dashboard.value,label:w.dashboard.label}:void 0,allowClear:!0,labelInValue:!0,onChange:ut,treeData:ke||[]}):(0,_.tZ)(z.qb,{ariaLabel:Te.DASHBOARD_TEXT,name:"dashboard",value:null!=w&&null!=(N=w.dashboard)&&N.label&&null!=w&&null!=(S=w.dashboard)&&S.value?{value:null==w||null==(x=w.dashboard)?void 0:x.value,label:null==w||null==(C=w.dashboard)?void 0:C.label}:void 0,options:nt||[],onChange:ut}),Me&&(0,_.tZ)(l.Fragment,null,(0,_.tZ)("div",{className:"inline-container"},(0,_.tZ)(pe,{onChange:e=>{const{target:t}=e;_e(t.value)},value:Ee},(0,_.tZ)(ue,{value:"PNG"},Te.SEND_AS_PNG_TEXT),(0,_.tZ)(ue,{value:"CSV"},Te.SEND_AS_CSV_TEXT),Y.includes(Xe)&&(0,_.tZ)(ue,{value:"TEXT"},Te.SEND_AS_TEXT)))),(i||"dashboard"===B)&&(0,_.tZ)("div",{className:"inline-container"},(0,_.tZ)(he,{"data-test":"bypass-cache",className:"checkbox",checked:Ze,onChange:e=>{fe(e.target.checked)}},Te.IGNORE_CACHE_TEXT)),(0,_.tZ)(se,null,(0,_.tZ)("h4",null,Te.NOTIFICATION_METHOD_TEXT),(0,_.tZ)("span",{className:"required"},"*")),Pe.map(((e,t)=>(0,_.tZ)(ve,null,(0,_.tZ)(K,{setting:e,index:t,key:`NotificationMethod-${t}`,onUpdate:je,onRemove:Ge})))),(0,_.tZ)(be,{"data-test":"notification-add",status:Ue,onClick:()=>{const e=Pe.slice();e.push({recipients:"",options:D}),ze(e),He(e.length===D.length?"hidden":"disabled")}})))))})),_e=(0,r.I)(),Ze={[f.Z.Success]:(0,o.t)("Success"),[f.Z.Working]:(0,o.t)("Working"),[f.Z.Error]:(0,o.t)("Error"),[f.Z.Noop]:(0,o.t)("Not triggered"),[f.Z.Grace]:(0,o.t)("On Grace")},fe=(0,i.Z)({requestType:"rison",method:"DELETE",endpoint:"/api/v1/report/"}),ye=s.iK.div`
  width: 100%;
  padding: 0 ${({theme:e})=>4*e.gridUnit}px
    ${({theme:e})=>3*e.gridUnit}px;
  background-color: ${({theme:e})=>e.colors.grayscale.light5};
`,Ne=s.iK.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  > *:first-child {
    margin-right: ${({theme:e})=>e.gridUnit}px;
  }
`,Se=_e.get("alertsreports.header.icon");const xe=(0,b.ZP)((function({addDangerToast:e,isReportEnabled:t=!1,user:a,addSuccessToast:r}){const i=t?(0,o.t)("report"):(0,o.t)("alert"),s=t?(0,o.t)("reports"):(0,o.t)("alerts"),d=t?"Reports":"Alerts",b=(0,l.useMemo)((()=>[{id:"type",operator:v.p.equals,value:t?"Report":"Alert"}]),[t]),{state:{loading:Z,resourceCount:y,resourceCollection:C,bulkSelectEnabled:A,lastFetched:w},hasPerm:I,fetchData:$,setResourceCollection:L,refreshData:M,toggleBulkSelect:U}=(0,O.Yi)("report",(0,o.t)("reports"),e,!0,void 0,b),{updateResource:H}=(0,O.LE)("report",(0,o.t)("reports"),e),[P,z]=(0,l.useState)(!1),[j,G]=(0,l.useState)(null),[q,W]=(0,l.useState)(null);function F(e){G(e),z(!0)}const V=I("can_write"),B=I("can_write"),K=I("can_write");(0,l.useEffect)((()=>{A&&B&&U()}),[t]);const J=[{id:"name",desc:!0}],Y=(0,l.useCallback)(((e,t)=>{if(null!=e&&e.id){const a=e.id,l=[...C];L(l.map((a=>(null==a?void 0:a.id)===e.id?{...a,active:t}:a))),H(a,{active:t},!1,!1).then().catch((()=>L(l)))}}),[C,L,H]),Q=(0,l.useMemo)((()=>[{Cell:({row:{original:{last_state:e}}})=>(0,_.tZ)(E.Z,{state:e,isReportEnabled:t}),accessor:"last_state",size:"xs",disableSortBy:!0},{Cell:({row:{original:{last_eval_dttm:e}}})=>e?u().utc(e).local().format(T.v2):"",accessor:"last_eval_dttm",Header:(0,o.t)("Last run"),size:"lg"},{accessor:"name",Header:(0,o.t)("Name"),size:"xl"},{Header:(0,o.t)("Schedule"),accessor:"crontab_humanized",size:"xl",Cell:({row:{original:{crontab_humanized:e="",timezone:t}}})=>(0,_.tZ)(m.u,{title:`${e} (${t})`,placement:"topLeft"},(0,_.tZ)("span",null,`${e} (${t})`))},{Cell:({row:{original:{recipients:e}}})=>e.map((e=>(0,_.tZ)(N,{key:e.id,type:e.type}))),accessor:"recipients",Header:(0,o.t)("Notification method"),disableSortBy:!0,size:"xl"},{Cell:({row:{original:{active:e}}})=>(0,_.tZ)(X.r,{disabled:!0,checked:e}),accessor:"active",Header:(0,o.t)("Active"),id:"active",disableSortBy:!0,size:"lg"},{Cell:({row:{original:{created_by:e}}})=>e&&e.cn_name?`${e.cn_name}`:e?`${e.first_name} ${e.last_name}`:"",Header:(0,o.t)("Created by"),id:"created_by",disableSortBy:!0,size:"xl"},{Cell:({row:{original:{owners:e=[]}}})=>(0,_.tZ)(h.Z,{users:e}),Header:(0,o.t)("Owners"),id:"owners",disableSortBy:!0,size:"xl"},{Cell:({row:{original:{changed_on_delta_humanized:e}}})=>(0,_.tZ)("span",{className:"no-wrap"},e),Header:(0,o.t)("Modified"),accessor:"changed_on_delta_humanized",size:"xl"},{Cell:({row:{original:e}})=>{const t=(0,n.k6)(),l=e.owners.map((e=>e.id)).includes(a.userId)||(0,R.i5)(a),r=[V?{label:"execution-log-action",tooltip:(0,o.t)("Execution log"),placement:"bottom",icon:"Note",onClick:()=>t.push(`/${e.type.toLowerCase()}/${e.id}/log`)}:null,V?{label:l?"edit-action":"preview-action",tooltip:l?(0,o.t)("Edit"):(0,o.t)("View"),placement:"bottom",icon:l?"Edit":"Binoculars",onClick:()=>F(e)}:null,l&&B?{label:"delete-action",tooltip:(0,o.t)("Delete"),placement:"bottom",icon:"Trash",onClick:()=>W(e)}:null].filter((e=>null!==e));return(0,_.tZ)(p.Z,{actions:r})},Header:(0,o.t)("Actions"),id:"actions",hidden:!V&&!B,disableSortBy:!0,size:"xl"}]),[B,V,t,Y]),ee=[];K&&ee.push({name:(0,_.tZ)(l.Fragment,null,(0,_.tZ)("i",{className:"fa fa-plus"})," ",i),buttonStyle:"primary",onClick:()=>{F(null)}}),B&&ee.push({name:(0,o.t)("Bulk select"),onClick:U,buttonStyle:"secondary","data-test":"bulk-select-toggle"});const te={title:(0,o.t)("No %s yet",s),image:"filter-results.svg",buttonAction:()=>F(null),buttonText:K?(0,_.tZ)(l.Fragment,null,(0,_.tZ)("i",{className:"fa fa-plus"})," ",i," "):null},ae=(0,l.useMemo)((()=>[{Header:(0,o.t)("Owner"),key:"owner",id:"owners",input:"select",operator:v.p.relationManyMany,unfilteredLabel:(0,o.t)("All"),fetchSelects:(0,k.tm)("report","owners",(0,k.v$)((e=>(0,o.t)("An error occurred while fetching owners values: %s",e))),a),paginate:!0},{Header:(0,o.t)("Created by"),key:"created_by",id:"created_by",input:"select",operator:v.p.relationOneMany,unfilteredLabel:"All",fetchSelects:(0,k.tm)("report","created_by",(0,k.v$)((e=>(0,o.t)("An error occurred while fetching created by values: %s",e))),a),paginate:!0},{Header:(0,o.t)("Status"),key:"status",id:"last_state",input:"select",operator:v.p.equals,unfilteredLabel:"Any",selects:[{label:Ze[f.Z.Success],value:f.Z.Success},{label:Ze[f.Z.Working],value:f.Z.Working},{label:Ze[f.Z.Error],value:f.Z.Error},{label:Ze[f.Z.Noop],value:f.Z.Noop},{label:Ze[f.Z.Grace],value:f.Z.Grace}]},{Header:(0,o.t)("Search"),key:"search",id:"name",input:"search",operator:v.p.contains}]),[]),le=Se?(0,_.tZ)(Ne,null,(0,_.tZ)("div",null,(0,o.t)("Alerts & reports")),(0,_.tZ)(Se,null)):(0,o.t)("Alerts & reports");return(0,_.tZ)("div",{style:{marginTop:"66px"}},(0,_.tZ)(g.Z,{activeChild:d,name:le,tabs:[{name:"Alerts",label:(0,o.t)("Alerts"),url:"/alert/list/",usesRouter:!0,"data-test":"alert-list"},{name:"Reports",label:(0,o.t)("Reports"),url:"/report/list/",usesRouter:!0,"data-test":"report-list"}],buttons:ee},(0,_.tZ)(ye,null,(0,_.tZ)(D,{updatedAt:w,update:()=>M()}))),(0,_.tZ)(Ee,{alert:j,addDangerToast:e,layer:j,onHide:()=>{z(!1),G(null),M()},show:P,isReport:t,key:(null==j?void 0:j.id)||`${(new Date).getTime()}`}),q&&(0,_.tZ)(x.Z,{description:(0,o.t)("This action will permanently delete %s.",q.name),onConfirm:()=>{q&&(({id:t,name:a})=>{c.Z.delete({endpoint:`/api/v1/report/${t}`}).then((()=>{M(),W(null),r((0,o.t)("Deleted: %s",a))}),(0,k.v$)((t=>e((0,o.t)("There was an issue deleting %s: %s",a,t)))))})(q)},onHide:()=>W(null),open:!0,title:(0,o.t)("Delete %s?",i)}),(0,_.tZ)(S.Z,{title:(0,o.t)("Please confirm"),description:(0,o.t)("Are you sure you want to delete the selected %s?",s),onConfirm:async t=>{try{const{message:e}=await fe(t.map((({id:e})=>e)));M(),r(e)}catch(t){(0,k.v$)((t=>e((0,o.t)("There was an issue deleting the selected %s: %s",s,t))))(t)}}},(e=>{const t=B?[{key:"delete",name:(0,o.t)("Delete"),onSelect:e,type:"danger"}]:[];return(0,_.tZ)(v.Z,{className:"alerts-list-view",columns:Q,count:y,data:C,emptyState:te,fetchData:$,filters:ae,initialSort:J,loading:Z,bulkActions:t,bulkSelectEnabled:A,disableBulkSelect:U,pageSize:25})})))}))},246714:(e,t,a)=>{a.d(t,{Z:()=>d});var l=a(751995),n=a(455867),r=(a(667294),a(358593)),o=a(731293),i=a(802849),s=a(211965);function c(e,t,a){switch(e){case i.Z.Working:return a.colors.primary.base;case i.Z.Error:return a.colors.error.base;case i.Z.Success:return t?a.colors.success.base:a.colors.alert.base;case i.Z.Noop:return a.colors.success.base;case i.Z.Grace:return a.colors.alert.base;default:return a.colors.grayscale.base}}function d({state:e,isReportEnabled:t=!1}){const a=(0,l.Fg)(),d={icon:o.Z.Check,label:"",status:""};switch(e){case i.Z.Success:d.icon=t?o.Z.Check:o.Z.AlertSolidSmall,d.label=t?(0,n.t)("Report sent"):(0,n.t)("Alert triggered, notification sent"),d.status=i.Z.Success;break;case i.Z.Working:d.icon=o.Z.Running,d.label=t?(0,n.t)("Report sending"):(0,n.t)("Alert running"),d.status=i.Z.Working;break;case i.Z.Error:d.icon=o.Z.XSmall,d.label=t?(0,n.t)("Report failed"):(0,n.t)("Alert failed"),d.status=i.Z.Error;break;case i.Z.Noop:d.icon=o.Z.Check,d.label=(0,n.t)("Nothing triggered"),d.status=i.Z.Noop;break;case i.Z.Grace:d.icon=o.Z.AlertSolidSmall,d.label=(0,n.t)("Alert Triggered, In Grace Period"),d.status=i.Z.Grace;break;default:d.icon=o.Z.Check,d.label=(0,n.t)("Nothing triggered"),d.status=i.Z.Noop}const u=d.icon;return(0,s.tZ)(r.u,{title:d.label,placement:"bottomLeft"},(0,s.tZ)(u,{iconColor:c(d.status,t,a)}))}},802849:(e,t,a)=>{var l,n;a.d(t,{Z:()=>l,u:()=>n}),function(e){e.Success="Success",e.Working="Working",e.Error="Error",e.Noop="Not triggered",e.Grace="On Grace"}(l||(l={})),function(e){e.Email="Email",e.Slack="Slack"}(n||(n={}))}}]);