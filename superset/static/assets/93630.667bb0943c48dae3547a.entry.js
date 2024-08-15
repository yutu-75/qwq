"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[93630],{596022:(e,t,a)=>{a.d(t,{ZN:()=>Y,gT:()=>X});var r=a(667294),n=a(828216),i=a(751995),o=a(211965),l=a(455867),s=a(731293),d=a(683862),c=a(601304),u=a(835932),p=a(414114),m=a(112515),g=a(456727),h=a(23525),y=a(710222),b=a(397634),v=a(591877),f=a(593185),Z=a(653002),x=a(915423),S=a(252655),w=a(9875),$=a(313433),k=a(427600),T=a(550909);const C=(0,i.iK)(T.qi)`
  && {
    margin: 0 0 ${({theme:e})=>e.gridUnit}px;
  }
`,_=({formData:e,addDangerToast:t})=>{const[a,n]=(0,r.useState)("400"),[i,s]=(0,r.useState)("600"),[d,c]=(0,r.useState)(""),[u,p]=(0,r.useState)(""),m=(0,r.useCallback)((e=>{const{value:t,name:a}=e.currentTarget;"width"===a&&s(t),"height"===a&&n(t)}),[]),g=(0,r.useCallback)((()=>{c(""),(0,h.YE)(e).then((e=>{c(e),p("")})).catch((()=>{p((0,l.t)("Error")),t((0,l.t)("Sorry, something went wrong. Try again later."))}))}),[t,e]);(0,r.useEffect)((()=>{g()}),[]);const y=(0,r.useMemo)((()=>{if(!d)return"";const e=`${d}?${k.KD.standalone.name}=1&height=${a}`;return`<iframe\n  width="${i}"\n  height="${a}"\n  seamless\n  frameBorder="0"\n  scrolling="no"\n  src="${e}"\n>\n</iframe>`}),[a,d,i]),b=u||y||(0,l.t)("Generating link, please wait..");return(0,o.tZ)("div",{id:"embed-code-popover","data-test":"embed-code-popover"},(0,o.tZ)("div",{css:o.iv`
          display: flex;
          flex-direction: column;
        `},(0,o.tZ)($.Z,{shouldShowText:!1,text:y,copyNode:(0,o.tZ)(C,{buttonSize:"xsmall"},(0,o.tZ)(S.default,null))}),(0,o.tZ)(w.Kx,{"data-test":"embed-code-textarea",name:"embedCode",disabled:!y,value:b,rows:"4",readOnly:!0,css:e=>o.iv`
            resize: vertical;
            padding: ${2*e.gridUnit}px;
            font-size: ${e.typography.sizes.s}px;
            border-radius: 4px;
            background-color: ${e.colors.secondary.light5};
          `})),(0,o.tZ)("div",{css:e=>o.iv`
          display: flex;
          margin-top: ${4*e.gridUnit}px;
          & > div {
            margin-right: ${2*e.gridUnit}px;
          }
          & > div:last-of-type {
            margin-right: 0;
            margin-left: ${2*e.gridUnit}px;
          }
        `},(0,o.tZ)("div",null,(0,o.tZ)("label",{htmlFor:"embed-height"},(0,l.t)("Chart height")),(0,o.tZ)(w.II,{type:"text",defaultValue:a,name:"height",onChange:m})),(0,o.tZ)("div",null,(0,o.tZ)("label",{htmlFor:"embed-width"},(0,l.t)("Chart width")),(0,o.tZ)(w.II,{type:"text",defaultValue:i,name:"width",onChange:m,id:"embed-width"}))))};var D=a(205872),I=a.n(D),U=a(473727);const E=({chartId:e,dashboards:t=[],...a})=>{const n=(0,i.Fg)(),[c,u]=(0,r.useState)(),[p,m]=(0,r.useState)(),g=t.length>10,h=t.filter((e=>!c||e.dashboard_title.toLowerCase().includes(c.toLowerCase()))),y=0===t.length,b=c&&0===h.length,v=e?`?focused_chart=${e}`:"";return(0,o.tZ)(r.Fragment,null,g&&(0,o.tZ)(w.II,{allowClear:!0,placeholder:(0,l.t)("Search"),prefix:(0,o.tZ)(s.Z.Search,{iconSize:"l"}),css:o.iv`
            width: ${220}px;
            margin: ${2*n.gridUnit}px ${3*n.gridUnit}px;
          `,value:c,onChange:e=>u(e.currentTarget.value)}),(0,o.tZ)("div",{css:o.iv`
          max-height: ${300}px;
          overflow: auto;
        `},h.map((e=>(0,o.tZ)(d.v2.Item,I()({key:String(e.id),onMouseEnter:()=>m(e.id),onMouseLeave:()=>{p===e.id&&m(null)}},a),(0,o.tZ)(U.rU,{target:"_blank",rel:"noreferer noopener",to:`/superset/dashboard/${e.id}${v}`},(0,o.tZ)("div",{css:o.iv`
                  display: flex;
                  flex-direction: row;
                  align-items: center;
                  max-width: ${220}px;
                `},(0,o.tZ)("div",{css:o.iv`
                    white-space: normal;
                  `},e.dashboard_title),(0,o.tZ)(s.Z.Full,{iconSize:"l",iconColor:n.colors.grayscale.base,css:o.iv`
                    margin-left: ${2*n.gridUnit}px;
                    visibility: ${p===e.id?"visible":"hidden"};
                  `})))))),b&&(0,o.tZ)("div",{css:o.iv`
              margin-left: ${3*n.gridUnit}px;
              margin-bottom: ${n.gridUnit}px;
            `},(0,l.t)("No results found")),y&&(0,o.tZ)(d.v2.Item,I()({disabled:!0,css:o.iv`
              min-width: ${220}px;
            `},a),(0,l.t)("None"))))};var M=a(920292),F=a(755961);const R=(0,M.Z)().common.conf.CHART_EXPORT_MAX_LIMIT||null,z="edit_properties",A="dashboards_added_to",N="download_submenu",P="export_to_csv",O="export_to_csv_pivoted",q="export_to_csv_whole",L="export_to_json",B="export_to_xlsx",j="export_to_whole",K="download_as_image",H="share_submenu",V="copy_permalink",W="embed_code",G="share_by_email",J="view_query",Q="run_in_sql_lab",Y=i.iK.div`
  ${({theme:e})=>o.iv`
    display: flex;
    align-items: center;

    & svg {
      width: ${3*e.gridUnit}px;
      height: ${3*e.gridUnit}px;
    }

    & span[role='checkbox'] {
      display: inline-flex;
      margin-right: ${e.gridUnit}px;
    }
  `}
`,X=((0,i.iK)(u.Z)`
  ${({theme:e})=>o.iv`
    width: ${8*e.gridUnit}px;
    height: ${8*e.gridUnit}px;
    padding: 0;
    border: 1px solid ${e.colors.primary.dark2};

    &.ant-btn > span.anticon {
      line-height: 0;
      transition: inherit;
    }

    &:hover:not(:focus) > span.anticon {
      color: ${e.colors.primary.light1};
    }
  `}
`,o.iv`
  .ant-dropdown-menu-item > & > .anticon:first-child {
    margin-right: 0;
    vertical-align: 0;
  }
`,(e,t,a,s,u,S,w)=>{const $=(0,i.Fg)(),{addDangerToast:k,addSuccessToast:T}=(0,p.e1)(),[C,D]=(0,r.useState)(null),[I,U]=(0,r.useState)(!1),[M,Y]=(0,r.useState)([]),X=(0,n.v9)((e=>{var t;return null==(t=e.charts)?void 0:t[(0,m.Jp)(e.explore)]})),{datasource:ee}=e,te=(0,r.useCallback)((async()=>{try{const t=(0,l.t)("Superset Chart"),a=await(0,h.YE)(e),r=encodeURIComponent((0,l.t)("%s%s","Check out this chart: ",a));window.location.href=`mailto:?Subject=${t}%20&Body=${r}`}catch(e){k((0,l.t)("Sorry, something went wrong. Try again later."))}}),[k,e]),ae=(0,r.useCallback)((()=>(0,m.pe)({formData:e,ownState:S,resultType:"full",resultFormat:"csv"})),[e]),re=(0,r.useCallback)((()=>t?(0,m.pe)({formData:e,resultType:"post_processed",resultFormat:"csv"}):null),[t,e]),ne=(0,r.useCallback)((()=>{const a={...e,row_limit:R};t&&(0,m.pe)({formData:a,resultType:"post_processed",resultFormat:"csv"})}),[t,e]),ie=(0,r.useCallback)((()=>(0,m.pe)({formData:e,resultType:"results",resultFormat:"json"})),[e]),oe=(0,r.useCallback)((()=>(0,m.pe)({formData:e,resultType:"results",resultFormat:"xlsx"})),[e]),le=(0,r.useCallback)((()=>{const t={...e,row_limit:R};(0,m.pe)({formData:t,resultType:"results",resultFormat:"xlsx"})}),[e]),se=(0,r.useCallback)((async()=>{try{if(!e)throw new Error;await(0,y.Z)((()=>(0,h.YE)(e))),T((0,l.t)("Copied to clipboard!"))}catch(e){k((0,l.t)("Sorry, something went wrong. Try again later."))}}),[k,T,e]),de=(0,r.useCallback)((({key:t,domEvent:r})=>{var n;switch(t){case z:u(),U(!1);break;case P:ae(),U(!1),Y([]);break;case O:re(),U(!1),Y([]);break;case q:ne(),U(!1),Y([]);break;case L:ie(),U(!1),Y([]);break;case B:oe(),U(!1),Y([]);break;case j:le(),U(!1),Y([]);break;case K:(0,g.Z)(".panel-body .chart-container",null!=(n=null==a?void 0:a.slice_name)?n:(0,l.t)("New chart"),!0)(r),U(!1),Y([]);break;case V:se(),U(!1),Y([]);break;case W:U(!1),Y([]);break;case G:te(),U(!1),Y([]);break;case J:U(!1);break;case Q:s(e),U(!1)}}),[se,ae,ie,e,s,u,te,null==a?void 0:a.slice_name]);return[(0,r.useMemo)((()=>(0,o.tZ)(d.v2,{onClick:de,selectable:!1,openKeys:M,onOpenChange:Y},(0,o.tZ)(r.Fragment,null,(0,o.tZ)(d.v2.SubMenu,{title:(0,l.t)("Dashboards added to"),key:A},(0,o.tZ)(E,{chartId:null==a?void 0:a.slice_id,dashboards:w})),(0,o.tZ)(d.v2.Divider,null)),(0,o.tZ)(d.v2.SubMenu,{title:(0,l.t)("Download"),key:N},(0,o.tZ)(F.Z,{position:"chart-edit",selectorString:null!=a&&a.slice_id?`#chart-id-${null==a?void 0:a.slice_id}`:".panel-body .chart-container",viz_type:null==e?void 0:e.viz_type,downLoadTitle:`${null==a?void 0:a.slice_name}`,latestQueryFormData:e,slice:a})),!1,(0,o.tZ)(d.v2.SubMenu,{title:(0,l.t)("Share"),key:H},(0,v.cr)(f.T.EMBEDDABLE_CHARTS)?(0,o.tZ)(d.v2.Item,{key:W},(0,o.tZ)(c.Z,{triggerNode:(0,o.tZ)("span",{"data-test":"embed-code-button"},(0,l.t)("Embed code")),modalTitle:(0,l.t)("Embed code"),modalBody:(0,o.tZ)(_,{formData:e,addDangerToast:k}),maxWidth:100*$.gridUnit+"px",destroyOnClose:!0,responsive:!0})):null),(0,o.tZ)(d.v2.Divider,null),C?(0,o.tZ)(r.Fragment,null,(0,o.tZ)(d.v2.SubMenu,{title:(0,l.t)("Manage email report")},(0,o.tZ)(b.Z,{chart:X,setShowReportSubMenu:D,showReportSubMenu:C,setIsDropdownVisible:U,isDropdownVisible:I,useTextMenu:!0})),(0,o.tZ)(d.v2.Divider,null)):(0,o.tZ)(d.v2,null,(0,o.tZ)(b.Z,{chart:X,setShowReportSubMenu:D,setIsDropdownVisible:U,isDropdownVisible:I,useTextMenu:!0})),(0,o.tZ)(d.v2.Item,{key:J},(0,o.tZ)(c.Z,{triggerNode:(0,o.tZ)("span",{"data-test":"view-query-menu-item"},(0,l.t)("View query")),modalTitle:(0,l.t)("View query"),modalBody:(0,o.tZ)(x.Z,{latestQueryFormData:e}),draggable:!0,resizable:!0,responsive:!0})),ee&&(0,Z.lI)("SQL Editor")&&(0,o.tZ)(d.v2.Item,{key:Q},(0,l.t)("Run in SQL Lab")))),[k,t,X,w,de,I,e,M,C,a,$.gridUnit]),I,U]})},109433:(e,t,a)=>{a.d(t,{CronPicker:()=>u});var r=a(205872),n=a.n(r),i=(a(667294),a(120271)),o=a(455867),l=a(751995),s=a(361247),d=a(211965);const c={everyText:(0,o.t)("every"),emptyMonths:(0,o.t)("every month"),emptyMonthDays:(0,o.t)("every day of the month"),emptyMonthDaysShort:(0,o.t)("day of the month"),emptyWeekDays:(0,o.t)("every day of the week"),emptyWeekDaysShort:(0,o.t)("day of the week"),emptyHours:(0,o.t)("every hour"),emptyMinutes:(0,o.t)("every minute"),emptyMinutesForHourPeriod:(0,o.t)("every"),yearOption:(0,o.t)("year"),monthOption:(0,o.t)("month"),weekOption:(0,o.t)("week"),dayOption:(0,o.t)("day"),hourOption:(0,o.t)("hour"),minuteOption:(0,o.t)("minute"),rebootOption:(0,o.t)("reboot"),prefixPeriod:(0,o.t)("Every"),prefixMonths:(0,o.t)("in"),prefixMonthDays:(0,o.t)("on"),prefixWeekDays:(0,o.t)("on"),prefixWeekDaysForMonthAndYearPeriod:(0,o.t)("and"),prefixHours:(0,o.t)("at"),prefixMinutes:(0,o.t)(":"),prefixMinutesForHourPeriod:(0,o.t)("at"),suffixMinutesForHourPeriod:(0,o.t)("minute(s)"),errorInvalidCron:(0,o.t)("Invalid cron expression"),clearButtonText:(0,o.t)("Clear"),weekDays:[(0,o.t)("Sunday"),(0,o.t)("Monday"),(0,o.t)("Tuesday"),(0,o.t)("Wednesday"),(0,o.t)("Thursday"),(0,o.t)("Friday"),(0,o.t)("Saturday")],months:[(0,o.t)("January"),(0,o.t)("February"),(0,o.t)("March"),(0,o.t)("April"),(0,o.t)("May"),(0,o.t)("June"),(0,o.t)("July"),(0,o.t)("August"),(0,o.t)("September"),(0,o.t)("October"),(0,o.t)("November"),(0,o.t)("December")],altWeekDays:[(0,o.t)("SUN"),(0,o.t)("MON"),(0,o.t)("TUE"),(0,o.t)("WED"),(0,o.t)("THU"),(0,o.t)("FRI"),(0,o.t)("SAT")],altMonths:[(0,o.t)("JAN"),(0,o.t)("FEB"),(0,o.t)("MAR"),(0,o.t)("APR"),(0,o.t)("MAY"),(0,o.t)("JUN"),(0,o.t)("JUL"),(0,o.t)("AUG"),(0,o.t)("SEP"),(0,o.t)("OCT"),(0,o.t)("NOV"),(0,o.t)("DEC")]},u=(0,l.iK)((e=>(0,d.tZ)(i.ZP,{getPopupContainer:e=>e.parentElement},(0,d.tZ)(s.default,n()({locale:c},e)))))`
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
`},188694:(e,t,a)=>{a.d(t,{$i:()=>m,Lt:()=>p});var r=a(205872),n=a.n(r),i=(a(667294),a(49937)),o=a(751995),l=a(731293),s=a(211965);const d=o.iK.div`
  width: ${({theme:e})=>.75*e.gridUnit}px;
  height: ${({theme:e})=>.75*e.gridUnit}px;
  border-radius: 50%;
  background-color: ${({theme:e})=>e.colors.grayscale.light1};

  font-weight: ${({theme:e})=>e.typography.weights.normal};
  display: inline-flex;
  position: relative;

  &:hover {
    background-color: ${({theme:e})=>e.colors.primary.base};

    &::before,
    &::after {
      background-color: ${({theme:e})=>e.colors.primary.base};
    }
  }

  &::before,
  &::after {
    position: absolute;
    content: ' ';
    width: ${({theme:e})=>.75*e.gridUnit}px;
    height: ${({theme:e})=>.75*e.gridUnit}px;
    border-radius: 50%;
    background-color: ${({theme:e})=>e.colors.grayscale.light1};
  }

  &::before {
    top: ${({theme:e})=>e.gridUnit}px;
  }

  &::after {
    bottom: ${({theme:e})=>e.gridUnit}px;
  }
`,c=o.iK.div`
  display: flex;
  align-items: center;
  padding: ${({theme:e})=>2*e.gridUnit}px;
  padding-left: ${({theme:e})=>e.gridUnit}px;
`;var u;!function(e){e.VERTICAL="vertical",e.HORIZONTAL="horizontal"}(u||(u={}));const p=({overlay:e,iconOrientation:t=u.VERTICAL,...a})=>(0,s.tZ)(i.Gj,n()({overlay:e},a),(0,s.tZ)(c,{"data-test":"dropdown-trigger"},((e=u.VERTICAL)=>e===u.HORIZONTAL?(0,s.tZ)(l.Z.MoreHoriz,{iconSize:"xl"}):(0,s.tZ)(d,null))(t))),m=e=>(0,s.tZ)(i.Gj,n()({overlayStyle:{zIndex:1001,animationDuration:"0s"}},e))},852564:(e,t,a)=>{a.d(t,{u:()=>$});var r=a(205872),n=a.n(r),i=a(667294),o=a(835932),l=a(616550),s=a(211965),d=a(455867),c=a(807500),u=a(667496),p=a(454076),m=a(49937),g=a(358593),h=a(899612);const y=e=>s.iv`
  display: flex;
  font-size: 18px;
  font-weight: ${e.typography.weights.bold};
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;

  & .dynamic-title,
  & .dynamic-title-input {
    display: inline-block;
    max-width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  & .dynamic-title {
    cursor: default;
  }
  & .dynamic-title-input {
    border: none;
    padding: 0;
    outline: none;

    &::placeholder {
      color: ${e.colors.grayscale.light1};
    }
  }

  & .input-sizer {
    position: absolute;
    left: -9999px;
    display: inline-block;
  }
`,b=({title:e,placeholder:t,onSave:a,canEdit:r,label:n})=>{const[o,l]=(0,i.useState)(!1),[c,u]=(0,i.useState)(e||""),p=(0,i.useRef)(null),[m,b]=(0,i.useState)(!1),{width:v,ref:f}=(0,h.NB)(),{width:Z,ref:x}=(0,h.NB)({refreshMode:"debounce"});(0,i.useEffect)((()=>{u(e)}),[e]),(0,i.useEffect)((()=>{if(o&&null!=p&&p.current&&(p.current.focus(),p.current.setSelectionRange)){const{length:e}=p.current.value;p.current.setSelectionRange(e,e),p.current.scrollLeft=p.current.scrollWidth}}),[o]),(0,i.useLayoutEffect)((()=>{null!=f&&f.current&&(f.current.innerHTML=(c||t).replace(/\s/g,"&nbsp;"))}),[c,t,f]),(0,i.useEffect)((()=>{p.current&&p.current.scrollWidth>p.current.clientWidth?b(!0):b(!1)}),[v,Z]);const S=(0,i.useCallback)((()=>{r&&!o&&l(!0)}),[r,o]),w=(0,i.useCallback)((()=>{if(!r)return;const t=c.trim();u(t),e!==t&&a(t),l(!1)}),[r,c,a,e]),$=(0,i.useCallback)((e=>{r&&o&&u(e.target.value)}),[r,o]),k=(0,i.useCallback)((e=>{var t;r&&("Enter"===e.key&&(e.preventDefault(),null==(t=p.current)||t.blur()))}),[r]);return(0,s.tZ)("div",{css:y,ref:x},(0,s.tZ)(g.u,{id:"title-tooltip",title:m&&c&&!o?c:null},r?(0,s.tZ)("input",{"data-test":"editable-title-input",className:"dynamic-title-input","aria-label":null!=n?n:(0,d.t)("Title"),ref:p,onChange:$,onBlur:w,onClick:S,onKeyPress:k,placeholder:t,value:c,css:s.iv`
              cursor: ${o?"text":"pointer"};

              ${v&&v>0&&s.iv`
                width: ${v+1}px;
              `}
            `}):(0,s.tZ)("span",{className:"dynamic-title","aria-label":null!=n?n:(0,d.t)("Title"),ref:p,"data-test":"editable-title"},c)),(0,s.tZ)("span",{ref:f,className:"input-sizer","aria-hidden":!0,tabIndex:-1}))};var v=a(679789),f=a(236674);const Z=e=>s.iv`
  display: flex;
  flex-direction: row;
  align-items: center;
  flex-wrap: nowrap;
  justify-content: space-between;
  // background-color: ${e.colors.grayscale.light5};
  background: #fefefe;
  // height: ${16*e.gridUnit}px;
  height: 48px;

  padding: 0 ${4*e.gridUnit}px;

  .editable-title {
    overflow: hidden;

    & > input[type='button'],
    & > span {
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 100%;
      white-space: nowrap;
    }
  }

  span[role='button'] {
    display: flex;
    height: 100%;
  }

  .title-panel {
    display: flex;
    align-items: center;
    min-width: 0;
    margin-right: ${12*e.gridUnit}px;
  }

  .right-button-panel {
    display: flex;
    align-items: center;
  }
`,x=e=>s.iv`
  display: flex;
  align-items: center;
  padding-left: ${2*e.gridUnit}px;

  & .fave-unfave-icon {
    padding: 0 ${e.gridUnit}px;

    &:first-of-type {
      padding-left: 0;
    }
  }
`,S=e=>s.iv`
  margin-left: ${2*e.gridUnit}px;
`,w=()=>{const e=(0,l.k6)();return(0,s.tZ)(o.Z,{style:{paddingLeft:"6px"},buttonStyle:"link",buttonSize:"default",onClick:()=>{e.goBack()},"data-test":"discard-changes-button","aria-label":(0,d.t)("Discard")},(0,s.tZ)("div",null,(0,s.tZ)(c.default,{title:"\u8fd4\u56de"})))},$=({backButtonProps:e=(0,s.tZ)(w,null),editableTitleProps:t,showTitlePanelItems:a,certificatiedBadgeProps:r,showFaveStar:o,faveStarProps:l,titlePanelAdditionalItems:c,rightPanelAdditionalItems:g,centerPanelAdditionalItems:h,subPanelAdditionalItems:y,additionalActionsMenu:$,menuDropdownProps:k,tooltipProps:T})=>(0,s.tZ)(i.Fragment,null,(0,s.tZ)("div",{css:Z,className:"header-with-actions",style:{...(0,p.w)()&&{marginTop:0}}},(0,s.tZ)("div",{className:"title-panel"},e,(0,s.tZ)(b,t),c,a&&(0,s.tZ)("div",{css:x},(null==r?void 0:r.certifiedBy)&&(0,s.tZ)(v.Z,r),o&&(0,s.tZ)(f.Z,l))),(0,s.tZ)("div",{className:"center-button-panel"},h),(0,s.tZ)("div",{className:"right-button-panel"},g,k&&(0,s.tZ)("div",{css:S},(0,s.tZ)(m.Gj,n()({trigger:["click"],overlay:$},k),(0,s.tZ)("div",{style:{display:"flex",alignItems:"center",cursor:"pointer"}},(0,s.tZ)("img",{style:{width:"20px",height:"20px",marginRight:"4px"},src:(0,u.VU)("/static/assets/images/more-unselected.png"),alt:""}),(0,s.tZ)("span",null,(0,d.t)("More"))))))),y)},397634:(e,t,a)=>{a.d(t,{x:()=>X,Z:()=>ae});var r,n,i=a(211965),o=a(667294),l=a(741427),s=a(828216),d=a(175049),c=a(751995),u=a(593185),p=a(455867),m=a(731293),g=a(112441),h=a(683862),y=a(787253),b=a(454076),v=a(188694),f=a(217198),Z=a(998286),x=a(161358),S=a(229487),w=a(898978),$=a(84367),k=a(414114);!function(e){e.DASHBOARDS="dashboards",e.CHARTS="charts"}(r||(r={})),function(e){e.TEXT="TEXT",e.PNG="PNG",e.CSV="CSV"}(n||(n={}));var T=a(34858),C=a(774069),_=a(835932),D=a(287183),I=a(109433);const U=(0,c.iK)(C.Z)`
  .ant-modal-body {
    padding: 0;
  }
`,E=c.iK.div`
  padding: ${({theme:e})=>`${3*e.gridUnit}px ${4*e.gridUnit}px ${2*e.gridUnit}px`};
  label {
    font-size: ${({theme:e})=>e.typography.sizes.s}px;
    color: ${({theme:e})=>e.colors.grayscale.light1};
  }
`,M=c.iK.div`
  border-top: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
  padding: ${({theme:e})=>`${4*e.gridUnit}px ${4*e.gridUnit}px ${6*e.gridUnit}px`};
  .ant-select {
    width: 100%;
  }
  .control-label {
    font-size: ${({theme:e})=>e.typography.sizes.s}px;
    color: ${({theme:e})=>e.colors.grayscale.light1};
  }
`,F=c.iK.span`
  span {
    margin-right: ${({theme:e})=>2*e.gridUnit}px;
    vertical-align: middle;
  }
  .text {
    vertical-align: middle;
  }
`,R=c.iK.div`
  margin-bottom: ${({theme:e})=>7*e.gridUnit}px;

  h4 {
    margin-bottom: ${({theme:e})=>3*e.gridUnit}px;
  }
`,z=(0,c.iK)(I.CronPicker)`
  margin-bottom: ${({theme:e})=>3*e.gridUnit}px;
  width: ${({theme:e})=>120*e.gridUnit}px;
`,A=c.iK.p`
  color: ${({theme:e})=>e.colors.error.base};
`,N=i.iv`
  margin-bottom: 0;
`,P=(0,c.iK)(_.Z)`
  width: ${({theme:e})=>40*e.gridUnit}px;
`,O=c.iK.div`
  margin: ${({theme:e})=>8*e.gridUnit}px 0
    ${({theme:e})=>4*e.gridUnit}px;
`,q=(0,c.iK)(D.Y)`
  display: block;
  line-height: ${({theme:e})=>8*e.gridUnit}px;
`,L=(0,c.iK)(D.Y.Group)`
  margin-left: ${({theme:e})=>.5*e.gridUnit}px;
`,B=["pivot_table","pivot_table_v2","table","paired_ttest"],j={crontab:"0 12 * * 1"};const K=(0,k.ZP)((function({onHide:e,show:t=!1,dashboardId:a,chart:r,userId:l,userEmail:d,creationMethod:c,dashboardName:u,chartName:g}){var h;const y=null==r||null==(h=r.sliceFormData)?void 0:h.viz_type,b=!!r,v=b&&y&&B.includes(y),f=v?n.TEXT:n.PNG,k=u||g,C=(0,o.useMemo)((()=>({...j,name:k?(0,p.t)("Weekly Report for %s",k):(0,p.t)("Weekly Report")})),[k]),_=(0,o.useCallback)(((e,t)=>"reset"===t?C:{...e,...t}),[C]),[D,I]=(0,o.useReducer)(_,C),[K,H]=(0,o.useState)(),V=(0,s.I0)(),W=(0,s.v9)((e=>{const t=a?X.DASHBOARDS:X.CHARTS;return(0,T._l)(e,t,a||(null==r?void 0:r.id))})),G=W&&Object.keys(W).length;(0,o.useEffect)((()=>{I(G?W:"reset")}),[G,W]);const J=(0,i.tZ)(F,null,(0,i.tZ)(m.Z.Calendar,null),(0,i.tZ)("span",{className:"text"},G?(0,p.t)("Edit email report"):(0,p.t)("Schedule a new email report"))),Q=(0,i.tZ)(o.Fragment,null,(0,i.tZ)(P,{key:"back",onClick:e},(0,p.t)("Cancel")),(0,i.tZ)(P,{key:"submit",buttonStyle:"primary",onClick:async()=>{const t={type:"Report",active:!0,force_screenshot:!1,creation_method:c,dashboard:a,chart:null==r?void 0:r.id,owners:[l],recipients:[{recipient_config_json:{target:d},type:"Email"}],name:D.name,description:D.description,crontab:D.crontab,report_format:D.report_format||f,timezone:D.timezone};I({isSubmitting:!0,error:void 0});try{G?await V((0,x.Me)(D.id,t)):await V((0,x.cq)(t)),e()}catch(e){const{error:t}=await(0,Z.O$)(e);I({error:t})}I({isSubmitting:!1})},disabled:!D.name,loading:D.isSubmitting},G?(0,p.t)("Save"):(0,p.t)("Add"))),Y=(0,i.tZ)(o.Fragment,null,(0,i.tZ)(O,null,(0,i.tZ)("h4",null,(0,p.t)("Message content"))),(0,i.tZ)("div",{className:"inline-container"},(0,i.tZ)(L,{onChange:e=>{I({report_format:e.target.value})},value:D.report_format||f},v&&(0,i.tZ)(q,{value:n.TEXT},(0,p.t)("Text embedded in email")),(0,i.tZ)(q,{value:n.PNG},(0,p.t)("Image (PNG) embedded in email")),(0,i.tZ)(q,{value:n.CSV},(0,p.t)("Formatted CSV attached in email")))));return(0,i.tZ)(U,{show:t,onHide:e,title:J,footer:Q,width:"432",centered:!0},(0,i.tZ)(E,null,(0,i.tZ)($.Z,{id:"name",name:"name",value:D.name||"",placeholder:C.name,required:!0,validationMethods:{onChange:({target:e})=>I({name:e.value})},label:(0,p.t)("Report Name"),"data-test":"report-name-test"}),(0,i.tZ)($.Z,{id:"description",name:"description",value:(null==D?void 0:D.description)||"",validationMethods:{onChange:({target:e})=>{I({description:e.value})}},label:(0,p.t)("Description"),placeholder:(0,p.t)("Include a description that will be sent with your report"),css:N,"data-test":"report-description-test"})),(0,i.tZ)(M,null,(0,i.tZ)(R,null,(0,i.tZ)("h4",{css:e=>(e=>i.iv`
  margin: ${3*e.gridUnit}px 0;
`)(e)},(0,p.t)("Schedule")),(0,i.tZ)("p",null,(0,p.t)("A screenshot of the dashboard will be sent to your email at"))),(0,i.tZ)(z,{clearButton:!1,value:D.crontab||"0 12 * * 1",setValue:e=>{I({crontab:e})},onError:H}),(0,i.tZ)(A,null,K),(0,i.tZ)("div",{className:"control-label",css:e=>(e=>i.iv`
  margin: ${3*e.gridUnit}px 0 ${2*e.gridUnit}px;
`)(e)},(0,p.t)("Timezone")),(0,i.tZ)(w.Z,{timezone:D.timezone,onTimezoneChange:e=>{I({timezone:e})}}),b&&Y),D.error&&(0,i.tZ)(S.Z,{type:"error",css:e=>(e=>i.iv`
  border: ${e.colors.error.base} 1px solid;
  padding: ${4*e.gridUnit}px;
  margin: ${4*e.gridUnit}px;
  margin-top: 0;
  color: ${e.colors.error.dark2};
  .ant-alert-message {
    font-size: ${e.typography.sizes.m}px;
    font-weight: bold;
  }
  .ant-alert-description {
    font-size: ${e.typography.sizes.m}px;
    line-height: ${4*e.gridUnit}px;
    .ant-alert-icon {
      margin-right: ${2.5*e.gridUnit}px;
      font-size: ${e.typography.sizes.l}px;
      position: relative;
      top: ${e.gridUnit/4}px;
    }
  }
`)(e),message:G?(0,p.t)("Failed to update report"):(0,p.t)("Failed to create report"),description:D.error}))}));var H=a(596022);const V=(0,d.I)(),W=e=>i.iv`
  color: ${e.colors.error.base};
`,G=e=>i.iv`
  & .ant-menu-item {
    padding: 5px 12px;
    margin-top: 0px;
    margin-bottom: 4px;
    :hover {
      color: ${e.colors.grayscale.dark1};
    }
  }
  :hover {
    background-color: ${e.colors.secondary.light5};
  }
`,J=e=>i.iv`
  &:hover {
    color: ${e.colors.grayscale.dark1};
    background-color: ${e.colors.secondary.light5};
  }
`,Q=c.iK.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  > *:first-child {
    margin-right: ${({theme:e})=>e.gridUnit}px;
  }
`,Y=V.get("report-modal.dropdown.item.icon");var X;!function(e){e.CHARTS="charts",e.DASHBOARDS="dashboards"}(X||(X={}));var ee={name:"1e1ncky",styles:"border:none"},te={name:"833hqy",styles:"width:200px"};function ae({dashboardId:e,chart:t,useTextMenu:a=!1,setShowReportSubMenu:r,setIsDropdownVisible:n,isDropdownVisible:d}){const Z=(0,s.I0)(),S=(0,s.v9)((a=>{const r=e?X.DASHBOARDS:X.CHARTS;return(0,T._l)(a,r,e||(null==t?void 0:t.id))})),w=(null==S?void 0:S.active)||!1,$=(0,s.v9)((e=>e.user)),k=()=>{if(!(0,u.c)(u.T.ALERT_REPORTS))return!1;if(null==$||!$.userId)return!1;return Object.keys($.roles||[]).map((e=>$.roles[e].filter((e=>"menu_access"===e[0]&&"Manage"===e[1])))).some((e=>e.length>0))},[C,_]=(0,o.useState)(null),D=(0,c.Fg)(),I=(0,l.D)(e),[U,E]=(0,o.useState)(!1),M=async(e,t)=>{null!=e&&e.id&&Z((0,x.M)(e,t))},F=k()&&!!(e&&I!==e||null!=t&&t.id);(0,o.useEffect)((()=>{F&&Z((0,x.Aw)({userId:$.userId,filterField:e?"dashboard_id":"chart_id",creationMethod:e?"dashboards":"charts",resourceId:e||(null==t?void 0:t.id)}))}),[]);const R=S&&r&&k();(0,o.useEffect)((()=>{R?r(!0):!S&&r&&r(!1)}),[S]);const z=()=>{n&&(n(!1),E(!0))},A=()=>{n&&(n(!1),_(S))};return(0,i.tZ)(o.Fragment,null,k()&&(0,i.tZ)(o.Fragment,null,(0,i.tZ)(K,{userId:$.userId,show:U,onHide:()=>E(!1),userEmail:$.email,dashboardId:e,chart:t,creationMethod:e?X.DASHBOARDS:X.CHARTS}),a?S?d&&(0,i.tZ)(h.v2,{selectable:!1,css:ee},(0,i.tZ)(h.v2.Item,{css:J,onClick:()=>M(S,!w)},(0,i.tZ)(H.ZN,null,(0,i.tZ)(y.ZP,{checked:w,onChange:b.EI}),(0,p.t)("Email reports active"))),(0,i.tZ)(h.v2.Item,{css:J,onClick:z},(0,p.t)("Edit email report")),(0,i.tZ)(h.v2.Item,{css:J,onClick:A},(0,p.t)("Delete email report"))):(0,i.tZ)(h.v2,{selectable:!1,css:G},(0,i.tZ)(h.v2.Item,{onClick:z},Y?(0,i.tZ)(Q,null,(0,i.tZ)("div",null,(0,p.t)("Set up an email report")),(0,i.tZ)(Y,null)):(0,p.t)("Set up an email report")),(0,i.tZ)(h.v2.Divider,null)):S?(0,i.tZ)(o.Fragment,null,(0,i.tZ)(v.$i,{overlay:(0,i.tZ)(h.v2,{selectable:!1,css:te},(0,i.tZ)(h.v2.Item,null,(0,p.t)("Email reports active"),(0,i.tZ)(g.r,{"data-test":"toggle-active",checked:w,onClick:e=>M(S,e),size:"small",css:(0,i.iv)({marginLeft:2*D.gridUnit},"","")})),(0,i.tZ)(h.v2.Item,{onClick:()=>E(!0)},(0,p.t)("Edit email report")),(0,i.tZ)(h.v2.Item,{onClick:()=>_(S),css:W},(0,p.t)("Delete email report"))),trigger:["click"],getPopupContainer:e=>e.closest(".action-button")},(0,i.tZ)("span",{role:"button",className:"action-button action-schedule-report",tabIndex:0},(0,i.tZ)(m.Z.Calendar,null)))):(0,i.tZ)("span",{role:"button",title:(0,p.t)("Schedule email report"),tabIndex:0,className:"action-button action-schedule-report",onClick:()=>E(!0)},(0,i.tZ)(m.Z.Calendar,null)),C&&(0,i.tZ)(f.Z,{description:(0,p.t)("This action will permanently delete %s.",null==C?void 0:C.name),onConfirm:()=>{C&&(async e=>{await Z((0,x.MZ)(e)),_(null)})(C)},onHide:()=>_(null),open:!0,title:(0,p.t)("Delete Report?")})))}},112441:(e,t,a)=>{a.d(t,{r:()=>l});a(667294);var r=a(751995),n=a(840987),i=a(211965);const o=(0,r.iK)(n.Z)`
  .ant-switch-checked {
    background-color: ${({theme:e})=>e.colors.primary.base};
  }
`,l=e=>(0,i.tZ)(o,e)},898978:(e,t,a)=>{a.d(t,{Z:()=>w});var r=a(211965),n=a(667294),i=a(480008),o=a.n(i),l=a(455867),s=a(49937);const d="GMT Standard Time",c="Africa/Abidjan",u="400px",p={"-300-240":["Eastern Standard Time","Eastern Daylight Time"],"-360-300":["Central Standard Time","Central Daylight Time"],"-420-360":["Mountain Standard Time","Mountain Daylight Time"],"-420-420":["Mountain Standard Time - Phoenix","Mountain Standard Time - Phoenix"],"-480-420":["Pacific Standard Time","Pacific Daylight Time"],"-540-480":["Alaska Standard Time","Alaska Daylight Time"],"-600-600":["Hawaii Standard Time","Hawaii Daylight Time"],60120:["Central European Time","Central European Daylight Time"],"00":[d,d],"060":["GMT Standard Time - London","British Summer Time"]},m=o()(),g=o()([2021,1]),h=o()([2021,7]),y=e=>g.tz(e).utcOffset().toString()+h.tz(e).utcOffset().toString(),b=e=>{var t,a;const r=y(e);return(m.tz(e).isDST()?null==(t=p[r])?void 0:t[1]:null==(a=p[r])?void 0:a[0])||e},v=o().tz.countries().map((e=>o().tz.zonesForCountry(e,!0))).flat(),f=[];v.forEach((e=>{f.find((t=>y(t.name)===y(e.name)))||f.push(e)}));const Z=f.map((e=>({label:`GMT ${o().tz(m,e.name).format("Z")} (${b(e.name)})`,value:e.name,offsets:y(e.name),timezoneName:e.name}))),x=(e,t)=>o().tz(m,e.timezoneName).utcOffset()-o().tz(m,t.timezoneName).utcOffset();Z.sort(x);const S=e=>{var t;return(null==(t=Z.find((t=>t.offsets===y(e))))?void 0:t.value)||c};function w({onTimezoneChange:e,timezone:t,minWidth:a=u}){const i=(0,n.useMemo)((()=>S(t||o().tz.guess())),[t]);return(0,n.useEffect)((()=>{t!==i&&e(i)}),[i,e,t]),(0,r.tZ)(s.Ph,{ariaLabel:(0,l.t)("Timezone selector"),css:(0,r.iv)({minWidth:a},"",""),onChange:t=>e(t),value:i,options:Z,sortComparator:x})}},987915:(e,t,a)=>{a.d(t,{U:()=>r,g:()=>n});const r=(e,t)=>Object.values(e).filter((e=>e[t])).reduce(((e,a)=>({...e,[a.id]:t?a[t]:a})),{}),n=({chartConfiguration:e,nativeFilters:t,dataMask:a,allSliceIds:r})=>{const n={};return Object.values(a).forEach((({id:a,extraFormData:i})=>{var o,l,s,d,c,u;const p=null!=(o=null!=(l=null!=(s=null==t||null==(d=t[a])?void 0:d.chartsInScope)?s:null==e||null==(c=e[a])||null==(u=c.crossFilters)?void 0:u.chartsInScope)?l:r)?o:[];n[a]={scope:p,values:i}})),n}},991914:(e,t,a)=>{a.d(t,{Z:()=>c});var r=a(301510),n=a(599543),i=a(269856);function o(e){return Object.entries(e).map((([e,t])=>{var a;let r="ILIKE",n=t;return Array.isArray(t)?r="IN":e.indexOf("__")>-1&&i.i2.hasOwnProperty(null==(a=e.split("__"))?void 0:a[1])?r="==":t&&(n=`%${t}%`),{col:e,op:r,val:n}})).filter((e=>null!==e.val&&""!==e.val))}var l=a(987915);const s={},d={};function c({chart:e,filters:t,nativeFilters:a,chartConfiguration:i,colorScheme:c,colorNamespace:u,sliceId:p,dataMask:m,extraControls:g,labelColors:h,sharedLabelColors:y,allSliceIds:b}){const v=d[p];if(s[p]===t&&(0,n.JB)(null==v?void 0:v.color_scheme,c,{ignoreUndefined:!0})&&(0,n.JB)(null==v?void 0:v.color_namespace,u,{ignoreUndefined:!0})&&(0,n.JB)(null==v?void 0:v.label_colors,h,{ignoreUndefined:!0})&&(0,n.JB)(null==v?void 0:v.shared_label_colors,y,{ignoreUndefined:!0})&&v&&(0,n.JB)(null==v?void 0:v.dataMask,m,{ignoreUndefined:!0})&&(0,n.JB)(null==v?void 0:v.extraControls,g,{ignoreUndefined:!0}))return v;let f={};const Z=(0,l.g)({chartConfiguration:i,dataMask:m,nativeFilters:a,allSliceIds:b}),x=Object.entries(Z).filter((([,{scope:t}])=>t.includes(e.id))).map((([e])=>e)),S=(0,r.Q)(p,a,m,x);x.length&&(f={extra_form_data:S.extraFormData});const w={...e.form_data,label_colors:h,shared_label_colors:y,...c&&{color_scheme:c},extra_filters:o(t),...f,...g};return s[p]=t,d[p]={...w,dataMask:m,extraControls:g},w}},95345:(e,t,a)=>{a.d(t,{c9:()=>P,Tg:()=>F});var r,n=a(667294),i=a(751995),o=a(455867),l=a(731293),s=a(171262),d=a(591877),c=a(593185),u=a(961337);!function(e){e.Results="results",e.Samples="samples"}(r||(r={}));var p=a(311064),m=a(355786),g=a(828216),h=a(838703),y=a(94301),b=a(935500),v=a(998286),f=a(676962),Z=a(550909),x=a(604788),S=a.n(x),w=a(88889),$=a(211965),k=a(454076),T=a(261587);const C=i.iK.div`
  ${({theme:e})=>`\n    display: flex;\n    align-items: center;\n    justify-content: space-between;\n    margin-bottom: ${2*e.gridUnit}px;\n\n    span {\n      flex-shrink: 0;\n    }\n  `}
`,_=({data:e,datasourceId:t,onInputChange:a,columnNames:r,columnTypes:i,isLoading:o})=>{const l=(0,T.W)(t),s=S()(r,i).filter((([e,t])=>t===w.Z.TEMPORAL&&e&&!l.includes(e))).map((([e])=>e)),d=(0,n.useMemo)((()=>(0,k.cD)(e,s)),[e,s]);return(0,$.tZ)(C,null,(0,$.tZ)(Z.HS,{onChangeHandler:a}),(0,$.tZ)("div",{css:$.iv`
          display: flex;
          align-items: center;
        `},(0,$.tZ)(Z.uy,{data:e,loading:o}),(0,$.tZ)(Z.m,{data:d,columns:r})))},D=({data:e,colnames:t,coltypes:a,datasourceId:r,dataSize:i=50,isVisible:l})=>{const[s,d]=(0,n.useState)(""),c=(0,Z._q)(t,a,e,r,l),u=(0,Z.C4)(s,e);return(0,$.tZ)(n.Fragment,null,(0,$.tZ)(_,{data:u,columnNames:t,columnTypes:a,datasourceId:r,onInputChange:e=>d(e),isLoading:!1}),(0,$.tZ)(f.Z,{columns:c,data:u,pageSize:i,noDataText:(0,o.t)("No results"),emptyWrapperType:f.u.Small,className:"table-condensed",isPaginationSticky:!0,showRowCount:!1,small:!0}))},I=i.iK.pre`
  margin-top: ${({theme:e})=>4*e.gridUnit+"px"};
`,U=new WeakMap,E=({isRequest:e,queryFormData:t,queryForce:a,ownState:r,errorMessage:i,actions:l,isVisible:s,dataSize:d=50})=>{var c,u;const f=(0,p.Z)().get((null==t?void 0:t.viz_type)||(null==t?void 0:t.vizType)),[Z,x]=(0,n.useState)([]),[S,w]=(0,n.useState)(!0),[k,T]=(0,n.useState)(""),C=null!=(c=null==f?void 0:f.queryObjectCount)?c:1,E=(0,g.v9)((e=>e)),M=null==E||null==(u=E.explore)?void 0:u.controls;if((0,n.useEffect)((()=>{i||(e&&U.has(t)&&(x((0,m.Z)(U.get(t))),T(""),a&&l&&l.setForceQuery(!1),w(!1)),e&&!U.has(t)&&(w(!0),(0,b.getChartDataRequest)({formData:t,force:a,resultFormat:"json",resultType:"results",ownState:r,controls:M}).then((({json:e})=>{x((0,m.Z)(e.result)),T(""),U.set(t,e.result),a&&l&&l.setForceQuery(!1)})).catch((e=>{(0,v.O$)(e).then((({error:e,message:t})=>{T(e||t||(0,o.t)("Sorry, an error occurred"))}))})).finally((()=>{w(!1)}))))}),[t,e]),(0,n.useEffect)((()=>{"big_number"===t.viz_type&&(w(!0),(0,b.getChartDataRequest)({formData:t,force:a,resultFormat:"json",resultType:"results",ownState:r,controls:M}).then((({json:e})=>{x((0,m.Z)(e.result)),T(""),U.set(t,e.result),a&&l&&l.setForceQuery(!1)})).catch((e=>{(0,v.O$)(e).then((({error:e,message:t})=>{T(e||t||(0,o.t)("Sorry, an error occurred"))}))})).finally((()=>{w(!1)})))}),[t.viz_type,e,M]),(0,n.useEffect)((()=>{i&&w(!1)}),[i]),S)return Array(C).fill((0,$.tZ)(h.Z,null));if(i){const e=(0,o.t)("Run a query to display results");return Array(C).fill((0,$.tZ)(y.x3,{image:"document.svg",title:e}))}if(k){const e=(0,$.tZ)(n.Fragment,null,(0,$.tZ)(_,{data:[],columnNames:[],columnTypes:[],datasourceId:t.datasource,onInputChange:()=>{},isLoading:!1}),(0,$.tZ)(I,null,k));return Array(C).fill(e)}if(0===Z.length){const e=(0,o.t)("No results were returned for this query");return Array(C).fill((0,$.tZ)(y.x3,{image:"document.svg",title:e}))}return Z.slice(0,C).map(((e,a)=>(0,$.tZ)(D,{data:e.data,colnames:e.colnames,coltypes:e.coltypes,dataSize:d,datasourceId:t.datasource,key:a,isVisible:s})))},M=i.iK.div`
  display: flex;
  flex-direction: column;
  height: 100%;

  .ant-tabs {
    height: 100%;
  }

  .ant-tabs-content {
    height: 100%;
  }

  .ant-tabs-tabpane {
    display: flex;
    flex-direction: column;
  }

  .table-condensed {
    overflow: auto;
  }
`,F=({isRequest:e,queryFormData:t,queryForce:a,ownState:n,errorMessage:i,actions:l,isVisible:d,dataSize:c=50})=>{const u=E({errorMessage:i,queryFormData:t,queryForce:a,ownState:n,isRequest:e,actions:l,dataSize:c,isVisible:d});if(1===u.length)return(0,$.tZ)(M,null,u[0]);const p=u.map(((e,t)=>0===t?(0,$.tZ)(s.ZP.TabPane,{tab:(0,o.t)("Results"),key:r.Results},e):(0,$.tZ)(s.ZP.TabPane,{tab:(0,o.t)("Results %s",t+1),key:`${r.Results} ${t+1}`},e)));return(0,$.tZ)(M,null,(0,$.tZ)(s.ZP,{fullWidth:!1},p))},R=i.iK.pre`
  margin-top: ${({theme:e})=>4*e.gridUnit+"px"};
`,z=new WeakSet,A=({isRequest:e,datasource:t,queryForce:a,actions:r,dataSize:i=50,isVisible:l})=>{const[s,d]=(0,n.useState)(""),[c,u]=(0,n.useState)([]),[p,g]=(0,n.useState)([]),[v,x]=(0,n.useState)([]),[S,w]=(0,n.useState)(!1),[k,T]=(0,n.useState)(""),C=(0,n.useMemo)((()=>`${t.id}__${t.type}`),[t]);(0,n.useEffect)((()=>{e&&a&&z.delete(t),e&&!z.has(t)&&(w(!0),(0,b.getDatasourceSamples)(t.type,t.id,a,{}).then((e=>{u((0,m.Z)(e.data)),g((0,m.Z)(e.colnames)),x((0,m.Z)(e.coltypes)),T(""),z.add(t),a&&r&&r.setForceQuery(!1)})).catch((e=>{u([]),g([]),x([]),T(`${e.name}: ${e.message}`)})).finally((()=>{w(!1)})))}),[t,e,a]);const D=(0,Z._q)(p,v,c,C,l),I=(0,Z.C4)(s,c);if(S)return(0,$.tZ)(h.Z,null);if(k)return(0,$.tZ)(n.Fragment,null,(0,$.tZ)(_,{data:I,columnNames:p,columnTypes:v,datasourceId:C,onInputChange:e=>d(e),isLoading:S}),(0,$.tZ)(R,null,k));if(0===c.length){const e=(0,o.t)("No samples were returned for this dataset");return(0,$.tZ)(y.x3,{image:"document.svg",title:e})}return(0,$.tZ)(n.Fragment,null,(0,$.tZ)(_,{data:I,columnNames:p,columnTypes:v,datasourceId:C,onInputChange:e=>d(e),isLoading:S}),(0,$.tZ)(f.Z,{columns:D,data:I,pageSize:i,noDataText:(0,o.t)("No results"),emptyWrapperType:f.u.Small,className:"table-condensed",isPaginationSticky:!0,showRowCount:!1,small:!0}))},N=i.iK.div`
  ${({theme:e})=>`\n    position: relative;\n    background-color: ${e.colors.grayscale.light5};\n    z-index: 11;\n    overflow: hidden;\n\n    .ant-tabs {\n      height: 100%;\n    }\n\n    .ant-tabs-content-holder {\n      height: 100%;\n    }\n\n    .ant-tabs-content {\n      height: 100%;\n    }\n\n    .ant-tabs-tabpane {\n      display: flex;\n      flex-direction: column;\n      height: 100%;\n\n      .table-condensed {\n        height: 100%;\n        overflow: auto;\n        margin-bottom: ${4*e.gridUnit}px;\n\n        .table {\n          margin-bottom: ${2*e.gridUnit}px;\n        }\n      }\n\n      .pagination-container > ul[role='navigation'] {\n        margin-top: 0;\n      }\n    }\n  `}
`,P=({queryFormData:e,datasource:t,queryForce:a,onCollapseChange:p,chartStatus:m,ownState:g,errorMessage:h,actions:y})=>{const b=(0,i.Fg)(),[v,f]=(0,n.useState)(r.Results),[Z,x]=(0,n.useState)({results:!1,samples:!1}),[S,w]=(0,n.useState)(!(0,d.cr)(c.T.DATAPANEL_CLOSED_BY_DEFAULT)&&(0,u.rV)(u.dR.is_datapanel_open,!1));(0,n.useEffect)((()=>{(0,d.cr)(c.T.DATAPANEL_CLOSED_BY_DEFAULT)||(0,u.LS)(u.dR.is_datapanel_open,S)}),[S]),(0,n.useEffect)((()=>{S||x({results:!1,samples:!1}),S&&v.startsWith(r.Results)&&"rendered"===m&&x({results:!0,samples:!1}),S&&v===r.Samples&&x({results:!1,samples:!0})}),[S,v,m]);const k=(0,n.useCallback)((e=>{p(e),w(e)}),[p]),T=(0,n.useCallback)(((e,t)=>{S?e===v&&(t.preventDefault(),k(!1)):k(!0),f(e)}),[v,k,S]),_=(0,n.useMemo)((()=>{const e=S?(0,$.tZ)(l.Z.CaretUp,{iconColor:b.colors.grayscale.base,"aria-label":(0,o.t)("Collapse data panel")}):(0,$.tZ)(l.Z.CaretDown,{iconColor:b.colors.grayscale.base,"aria-label":(0,o.t)("Expand data panel")});return(0,$.tZ)(C,null,S?(0,$.tZ)("span",{role:"button",tabIndex:0,onClick:()=>k(!1)},e):(0,$.tZ)("span",{role:"button",tabIndex:0,onClick:()=>k(!0)},e))}),[k,S,b.colors.grayscale.base]),D=E({errorMessage:h,queryFormData:e,queryForce:a,ownState:g,isRequest:Z.results,actions:y,isVisible:r.Results===v}).map(((e,t)=>0===t?(0,$.tZ)(s.ZP.TabPane,{tab:(0,o.t)("Results"),key:r.Results},e):t>0?(0,$.tZ)(s.ZP.TabPane,{tab:(0,o.t)("Results %s",t+1),key:`${r.Results} ${t+1}`},e):null));return(0,$.tZ)(N,{"data-test":"some-purposeful-instance"},(0,$.tZ)(s.ZP,{fullWidth:!1,tabBarExtraContent:_,activeKey:S?v:"",onTabClick:T},D,(0,$.tZ)(s.ZP.TabPane,{tab:(0,o.t)("Samples"),key:r.Samples},(0,$.tZ)(A,{datasource:t,queryForce:a,isRequest:Z.samples,actions:y,isVisible:r.Samples===v}))))}},915423:(e,t,a)=>{a.d(t,{Z:()=>m});var r=a(667294),n=a(751995),i=a(355786),o=a(455867),l=a(838703),s=a(998286),d=a(935500),c=a(985626),u=a(211965);const p=n.iK.div`
  height: 100%;
  display: flex;
  flex-direction: column;
`,m=e=>{const[t,a]=(0,r.useState)([]),[n,m]=(0,r.useState)(!1),[g,h]=(0,r.useState)(null);return(0,r.useEffect)((()=>{var t;t="query",m(!0),(0,d.getChartDataRequest)({formData:e.latestQueryFormData,resultFormat:"json",resultType:t}).then((({json:e})=>{a((0,i.Z)(e.result)),m(!1),h(null)})).catch((e=>{(0,s.O$)(e).then((({error:t,message:a})=>{h(t||a||e.statusText||(0,o.t)("Sorry, An error occurred")),m(!1)}))}))}),[JSON.stringify(e.latestQueryFormData)]),n?(0,u.tZ)(l.Z,null):g?(0,u.tZ)("pre",null,g):(0,u.tZ)(p,null,t.map((e=>e.query?(0,u.tZ)(c.Z,{sql:e.query,language:e.language||void 0}):null)))}},428615:(e,t,a)=>{a.d(t,{S:()=>i});var r=a(667294),n=a(741427);function i(e,t){const a=(0,n.D)(e);(0,r.useEffect)((()=>{e!==a&&t(a,e)}),[e,a,t])}},906954:(e,t,a)=>{a.d(t,{z:()=>l});var r=a(667294),n=a(714670),i=a.n(n);const o=new(a(311133).g0)("tab_id_channel");function l(){const[e,t]=(0,r.useState)();return(0,r.useEffect)((()=>{if(!function(){try{return window.localStorage&&window.sessionStorage}catch(e){return!1}}())return void(e||t(i().generate()));const a=()=>{const e=window.localStorage.getItem("last_tab_id"),a=String(e?Number.parseInt(e,10)+1:1);window.sessionStorage.setItem("tab_id",a),window.localStorage.setItem("last_tab_id",a),t(a)},r=window.sessionStorage.getItem("tab_id");r?(o.postMessage({type:"REQUESTING_TAB_ID",tabId:r}),t(r)):a(),o.onmessage=t=>{if(t.tabId===e)if("REQUESTING_TAB_ID"===t.type){const e={type:"TAB_ID_DENIED",tabId:t.tabId};o.postMessage(e)}else"TAB_ID_DENIED"===t.type&&a()}}),[e]),e}}}]);