(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[20987],{313433:(e,t,n)=>{"use strict";n.d(t,{Z:()=>v});var o=n(667294),r=n(45697),a=n.n(r),i=n(455867),l=n(358593),s=n(414114),c=n(710222),d=n(211965);const u={copyNode:a().node,getText:a().func,onCopyEnd:a().func,shouldShowText:a().bool,text:a().string,wrapped:a().bool,tooltipText:a().string,addDangerToast:a().func.isRequired,addSuccessToast:a().func.isRequired,hideTooltip:a().bool},g={copyNode:(0,d.tZ)("span",null,(0,i.t)("Copy")),onCopyEnd:()=>{},shouldShowText:!0,wrapped:!0,tooltipText:(0,i.t)("Copy to clipboard"),hideTooltip:!1};var p={name:"8irbms",styles:"display:inline-flex;align-items:center"};class h extends o.Component{constructor(e){super(e),this.copyToClipboard=this.copyToClipboard.bind(this),this.onClick=this.onClick.bind(this)}onClick(){this.props.getText?this.props.getText((e=>{this.copyToClipboard(Promise.resolve(e))})):this.copyToClipboard(Promise.resolve(this.props.text))}getDecoratedCopyNode(){return o.cloneElement(this.props.copyNode,{style:{cursor:"pointer"},onClick:this.onClick})}copyToClipboard(e){(0,c.Z)((()=>e)).then((()=>{this.props.addSuccessToast((0,i.t)("Copied to clipboard!"))})).catch((()=>{this.props.addDangerToast((0,i.t)("Sorry, your browser does not support copying. Use Ctrl / Cmd + C!"))})).finally((()=>{this.props.onCopyEnd()}))}renderTooltip(e){return(0,d.tZ)(o.Fragment,null,this.props.hideTooltip?this.getDecoratedCopyNode():(0,d.tZ)(l.u,{id:"copy-to-clipboard-tooltip",placement:"topRight",style:{cursor:e},title:this.props.tooltipText,trigger:["hover"],arrowPointAtCenter:!0},this.getDecoratedCopyNode()))}renderNotWrapped(){return this.renderTooltip("pointer")}renderLink(){return(0,d.tZ)("span",{css:p},this.props.shouldShowText&&this.props.text&&(0,d.tZ)("span",{className:"m-r-5","data-test":"short-url"},this.props.text),this.renderTooltip())}render(){const{wrapped:e}=this.props;return e?this.renderLink():this.renderNotWrapped()}}const v=(0,s.ZP)(h);h.propTypes=u,h.defaultProps=g},835932:(e,t,n)=>{"use strict";n.d(t,{Z:()=>v});var o=n(205872),r=n.n(o),a=n(211965),i=n(121804),l=n.n(i),s=n(667294),c=n(898034),d=n(294184),u=n.n(d),g=n(49937),p=n(751995),h=n(358593);function v(e){const{tooltip:t,placement:n,disabled:o=!1,buttonSize:i,buttonStyle:d,className:v,cta:f,children:m,href:_,showMarginRight:b=!0,...R}=e,E=(0,p.Fg)(),{colors:O,transitionTiming:N,borderRadius:C,typography:S}=E,{primary:y,grayscale:x,success:T,warning:w,error:Z}=O;let A=32,I=18;"xsmall"===i?(A=22,I=5):"small"===i&&(A=30,I=10);let $=y.light4,k=(0,c.CD)(.1,y.base,y.light4),D=(0,c.CD)(.25,y.base,y.light4),P=x.light2,U=y.dark1,L=U,M=0,z="none",W="transparent",F="transparent",q="transparent";"primary"===d?($=y.base,k=y.light1,D=(0,c.CD)(.2,x.dark2,y.dark1),U=x.light5,L=U):"tertiary"===d||"dashed"===d?($=x.light5,k=x.light5,D=x.light5,P=x.light5,M=1,z="dashed"===d?"dashed":"solid",W=y.dark1,F=y.light1,q=x.light2):"danger"===d?($=Z.base,k=(0,c.CD)(.1,x.light5,Z.base),D=(0,c.CD)(.2,x.dark2,Z.base),U=x.light5,L=U):"warning"===d?($=w.base,k=(0,c.CD)(.1,x.dark2,w.base),D=(0,c.CD)(.2,x.dark2,w.base),U=x.light5,L=U):"success"===d?($=T.base,k=(0,c.CD)(.1,x.light5,T.base),D=(0,c.CD)(.2,x.dark2,T.base),U=x.light5,L=U):"link"===d&&($="transparent",k="transparent",D="transparent",L=y.base);const K=m;let B=[];B=K&&K.type===s.Fragment?s.Children.toArray(K.props.children):s.Children.toArray(m);const G=b&&B.length>1?2*E.gridUnit:0,V=(0,a.tZ)(g.C0,r()({href:o?void 0:_,disabled:o,className:u()(v,"superset-button",{cta:!!f}),css:(0,a.iv)({display:"inline-flex",alignItems:"center",justifyContent:"center",lineHeight:1.5715,fontSize:S.sizes.s,fontWeight:S.weights.bold,height:A,textTransform:"uppercase",padding:`0px ${I}px`,transition:`all ${N}s`,minWidth:f?36*E.gridUnit:void 0,minHeight:f?8*E.gridUnit:void 0,boxShadow:"none",borderWidth:M,borderStyle:z,borderColor:W,borderRadius:C,color:U,backgroundColor:$,"&:hover":{color:L,backgroundColor:k,borderColor:F},"&:active":{color:U,backgroundColor:D},"&:focus":{color:U,backgroundColor:$,borderColor:W},"&[disabled], &[disabled]:hover":{color:x.base,backgroundColor:"link"===d?"transparent":P,borderColor:"link"===d?"transparent":q,pointerEvents:"none"},marginLeft:0,"& + .superset-button":{marginLeft:2*E.gridUnit},"& > :first-of-type":{marginRight:G}},"","")},R),m);return t?(0,a.tZ)(h.u,{placement:n,id:`${l()(t)}-tooltip`,title:t},o?(0,a.tZ)("span",{css:(0,a.iv)({cursor:"not-allowed","& > .superset-button":{marginLeft:2*E.gridUnit}},"","")},V):V):V}},891178:(e,t,n)=>{"use strict";n.d(t,{Z:()=>v});var o=n(667294),r=n(751995),a=n(455867),i=n(454076),l=n(774069),s=n(835932),c=n(731293),d=n(313433),u=n(211965);const g=r.iK.div`
  background-color: ${({level:e,theme:t})=>t.colors[e].light2};
  border-radius: ${({theme:e})=>e.borderRadius}px;
  border: 1px solid ${({level:e,theme:t})=>t.colors[e].base};
  color: ${({level:e,theme:t})=>t.colors[e].dark2};
  padding: ${({theme:e})=>2*e.gridUnit}px;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;

  .top-row {
    display: flex;
    justify-content: space-between;
  }

  .error-body {
    overflow: auto;
    padding-top: ${({theme:e})=>e.gridUnit}px;
    padding-left: ${({theme:e})=>8*e.gridUnit}px;
  }

  .icon {
    margin-right: ${({theme:e})=>2*e.gridUnit}px;
  }

  .link {
    color: ${({level:e,theme:t})=>t.colors[e].dark2};
    text-decoration: underline;
  }
`,p=(0,r.iK)(l.Z)`
  color: ${({level:e,theme:t})=>t.colors[e].dark2};
  overflow-wrap: break-word;

  .ant-modal-header {
    background-color: ${({level:e,theme:t})=>t.colors[e].light2};
    padding: ${({theme:e})=>4*e.gridUnit}px;
  }

  .icon {
    margin-right: ${({theme:e})=>2*e.gridUnit}px;
  }

  .header {
    display: flex;
    align-items: center;
    font-size: ${({theme:e})=>e.typography.sizes.l}px;
  }
`,h=r.iK.div`
  align-items: center;
  display: flex;
`;function v({body:e,copyText:t,level:n="error",source:l="dashboard",subtitle:v,title:f,description:m}){const _=(0,r.Fg)(),[b,R]=(0,o.useState)(!1),[E,O]=(0,o.useState)(!1),N=["explore","sqllab"].includes(l),C=_.colors[n].base;return(0,u.tZ)(g,{level:n,role:"alert"},(0,u.tZ)("div",{className:"top-row"},(0,u.tZ)(h,null,"error"===n?(0,u.tZ)(c.Z.ErrorSolid,{className:"icon",iconColor:C}):(0,u.tZ)(c.Z.WarningSolid,{className:"icon",iconColor:C}),(0,u.tZ)("strong",null,f)),!N&&!m&&(0,u.tZ)("span",{role:"button",tabIndex:0,className:"link",onClick:()=>R(!0)},(0,a.t)("See more"))),m&&(0,u.tZ)("div",{className:"error-body"},(0,u.tZ)("p",null,m),!N&&(0,u.tZ)("span",{role:"button",tabIndex:0,className:"link",onClick:()=>R(!0)},(0,a.t)("See more"))),N?(0,u.tZ)("div",{className:"error-body"},(0,u.tZ)("p",null,v),e&&(0,u.tZ)(o.Fragment,null,!E&&(0,u.tZ)("span",{role:"button",tabIndex:0,className:"link",onClick:()=>O(!0)},(0,a.t)("See more")),E&&(0,u.tZ)(o.Fragment,null,(0,u.tZ)("br",null),e,(0,u.tZ)("span",{role:"button",tabIndex:0,className:"link",onClick:()=>O(!1)},(0,a.t)("See less"))))):(0,u.tZ)(p,{level:n,show:b,onHide:()=>R(!1),title:(0,u.tZ)("div",{className:"header"},"error"===n?(0,u.tZ)(c.Z.ErrorSolid,{className:"icon",iconColor:C}):(0,u.tZ)(c.Z.WarningSolid,{className:"icon",iconColor:C}),(0,u.tZ)("div",{className:"title"},f)),footer:(0,u.tZ)(o.Fragment,null,t&&(0,u.tZ)(d.Z,{text:t,shouldShowText:!1,wrapped:!1,copyNode:(0,u.tZ)(s.Z,{onClick:i.EI},(0,a.t)("Copy message"))}),(0,u.tZ)(s.Z,{cta:!0,buttonStyle:"primary",onClick:()=>R(!1)},(0,a.t)("Close")))},(0,u.tZ)(o.Fragment,null,(0,u.tZ)("p",null,v),v&&e&&(0,u.tZ)("br",null),e)))}},792869:(e,t,n)=>{"use strict";n.d(t,{Z:()=>i});var o=n(590537),r=n(601875);class a extends o.Z{constructor(){super({name:"ErrorMessageComponent",overwritePolicy:o.r.ALLOW})}}const i=(0,r.Z)(a)},167663:(e,t,n)=>{"use strict";n.d(t,{C:()=>o});const o={FRONTEND_CSRF_ERROR:"FRONTEND_CSRF_ERROR",FRONTEND_NETWORK_ERROR:"FRONTEND_NETWORK_ERROR",FRONTEND_TIMEOUT_ERROR:"FRONTEND_TIMEOUT_ERROR",GENERIC_DB_ENGINE_ERROR:"GENERIC_DB_ENGINE_ERROR",COLUMN_DOES_NOT_EXIST_ERROR:"COLUMN_DOES_NOT_EXIST_ERROR",TABLE_DOES_NOT_EXIST_ERROR:"TABLE_DOES_NOT_EXIST_ERROR",SCHEMA_DOES_NOT_EXIST_ERROR:"SCHEMA_DOES_NOT_EXIST_ERROR",CONNECTION_INVALID_USERNAME_ERROR:"CONNECTION_INVALID_USERNAME_ERROR",CONNECTION_INVALID_PASSWORD_ERROR:"CONNECTION_INVALID_PASSWORD_ERROR",CONNECTION_INVALID_HOSTNAME_ERROR:"CONNECTION_INVALID_HOSTNAME_ERROR",CONNECTION_PORT_CLOSED_ERROR:"CONNECTION_PORT_CLOSED_ERROR",CONNECTION_INVALID_PORT_ERROR:"CONNECTION_INVALID_PORT_ERROR",CONNECTION_HOST_DOWN_ERROR:"CONNECTION_HOST_DOWN_ERROR",CONNECTION_ACCESS_DENIED_ERROR:"CONNECTION_ACCESS_DENIED_ERROR",CONNECTION_UNKNOWN_DATABASE_ERROR:"CONNECTION_UNKNOWN_DATABASE_ERROR",CONNECTION_DATABASE_PERMISSIONS_ERROR:"CONNECTION_DATABASE_PERMISSIONS_ERROR",CONNECTION_MISSING_PARAMETERS_ERRORS:"CONNECTION_MISSING_PARAMETERS_ERRORS",OBJECT_DOES_NOT_EXIST_ERROR:"OBJECT_DOES_NOT_EXIST_ERROR",SYNTAX_ERROR:"SYNTAX_ERROR",VIZ_GET_DF_ERROR:"VIZ_GET_DF_ERROR",UNKNOWN_DATASOURCE_TYPE_ERROR:"UNKNOWN_DATASOURCE_TYPE_ERROR",FAILED_FETCHING_DATASOURCE_INFO_ERROR:"FAILED_FETCHING_DATASOURCE_INFO_ERROR",TABLE_SECURITY_ACCESS_ERROR:"TABLE_SECURITY_ACCESS_ERROR",DATASOURCE_SECURITY_ACCESS_ERROR:"DATASOURCE_SECURITY_ACCESS_ERROR",DATABASE_SECURITY_ACCESS_ERROR:"DATABASE_SECURITY_ACCESS_ERROR",QUERY_SECURITY_ACCESS_ERROR:"QUERY_SECURITY_ACCESS_ERROR",MISSING_OWNERSHIP_ERROR:"MISSING_OWNERSHIP_ERROR",BACKEND_TIMEOUT_ERROR:"BACKEND_TIMEOUT_ERROR",DATABASE_NOT_FOUND_ERROR:"DATABASE_NOT_FOUND_ERROR",MISSING_TEMPLATE_PARAMS_ERROR:"MISSING_TEMPLATE_PARAMS_ERROR",INVALID_TEMPLATE_PARAMS_ERROR:"INVALID_TEMPLATE_PARAMS_ERROR",RESULTS_BACKEND_NOT_CONFIGURED_ERROR:"RESULTS_BACKEND_NOT_CONFIGURED_ERROR",DML_NOT_ALLOWED_ERROR:"DML_NOT_ALLOWED_ERROR",INVALID_CTAS_QUERY_ERROR:"INVALID_CTAS_QUERY_ERROR",INVALID_CVAS_QUERY_ERROR:"INVALID_CVAS_QUERY_ERROR",SQLLAB_TIMEOUT_ERROR:"SQLLAB_TIMEOUT_ERROR",RESULTS_BACKEND_ERROR:"RESULTS_BACKEND_ERROR",ASYNC_WORKERS_ERROR:"ASYNC_WORKERS_ERROR",GENERIC_COMMAND_ERROR:"GENERIC_COMMAND_ERROR",GENERIC_BACKEND_ERROR:"GENERIC_BACKEND_ERROR",INVALID_PAYLOAD_FORMAT_ERROR:"INVALID_PAYLOAD_FORMAT_ERROR",INVALID_PAYLOAD_SCHEMA_ERROR:"INVALID_PAYLOAD_SCHEMA_ERROR"}},731293:(e,t,n)=>{"use strict";n.d(t,{Z:()=>_});var o=n(205872),r=n.n(o),a=n(318029),i=n.n(a),l=n(667294),s=n(362816),c=n(653014),d=n(751995);function u(){return u=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var o in n)Object.prototype.hasOwnProperty.call(n,o)&&(e[o]=n[o])}return e},u.apply(this,arguments)}const g=function(e){return l.createElement("svg",u({width:24,height:24,viewBox:"0 0 24 24",fill:"none",xmlns:"http://www.w3.org/2000/svg"},e))};var p=n(211965);const h=(0,d.iK)((({iconColor:e,iconSize:t,viewBox:n,...o})=>(0,p.tZ)(c.Z,r()({viewBox:n||"0 0 24 24"},o))))`
  ${({iconColor:e})=>e&&`color: ${e};`};
  font-size: ${({iconSize:e,theme:t})=>e?`${t.typography.sizes[e]||t.typography.sizes.m}px`:"24px"};
`,v=e=>{const{fileName:t,...o}=e,[,a]=(0,l.useState)(!1),i=(0,l.useRef)(),s=t.replace("_","-");return(0,l.useEffect)((()=>{let e=!1;return async function(){i.current=(await n(335782)(`./${t}.svg`)).default,e||a(!0)}(),()=>{e=!0}}),[t,i]),(0,p.tZ)(h,r()({component:i.current||g,"aria-label":s},o))},f=Object.keys(s).filter((e=>!e.includes("TwoTone"))).map((e=>({[e]:t=>(0,p.tZ)(h,r()({component:s[e]},t))}))).reduce(((e,t)=>({...e,...t}))),m={};["alert","alert_solid","alert_solid_small","area-chart-tile","bar-chart-tile","big-number-chart-tile","binoculars","bolt","bolt_small","bolt_small_run","calendar","cancel","cancel_solid","cancel-x","card_view","cards","cards_locked","caret_down","caret_left","caret_right","caret_up","caret_edit","caret_more","caret_delete","certified","check","checkbox-half","checkbox-off","checkbox-on","circle_check","circle_check_solid","circle","clock","close","code","cog","collapse","color_palette","current-rendered-tile","components","copy","cursor_target","database","dataset_physical","dataset_virtual_greyscale","dataset_virtual","download","drag","edit_alt","edit","email","error","error_solid","error_solid_small","exclamation","expand","eye","eye_slash","favorite-selected","favorite_small_selected","favorite-unselected","field_abc","field_boolean","field_date","field_derived","field_num","field_struct","file","filter","filter_small","folder","full","function_x","gear","grid","image","import","info","info-solid","info_solid_small","join","keyboard","layers","lightbulb","line-chart-tile","link","list","list_view","location","lock_locked","lock_unlocked","map","message","minus","minus_solid","more_horiz","more_vert","move","nav_charts","nav_dashboard","nav_data","nav_explore","nav_home","nav_lab","note","offline","paperclip","pie-chart-tile","placeholder","plus","plus_large","plus_small","plus_solid","queued","refresh","running","save","sql","search","server","share","slack","sort_asc","sort_desc","sort","table","table-chart-tile","tag","trash","triangle_change","triangle_down","triangle_up","up-level","user","warning","warning_solid","x-large","x-small","tags","ballot","category","undo","redo","dash-style","auto-resize","reload","left-do","right-do","more","chart","layout-element","filter-com","full-screen","edit-icon","recent-sort","view-sort","name-sort","data-sort","review","view-search","more-setting","fangda","filter-icon","view-detail","share-icon","download-icon","tiaozhuan-setting","header-icon","component-style","gou","shunxu","zhiding","zhidi","upone","downone","delete-icon","database-menu","database-api","dashbord-pcicon","chart-pcicon","dataset-sqlicon","dataset-sqllicon","dataset-excleicon","dataset-unionicon","folder-m","file-m"].forEach((e=>{const t=i()(e).replace(/ /g,"");m[t]=t=>(0,p.tZ)(v,r()({fileName:e},t))}));const _={...f,...m}},838703:(e,t,n)=>{"use strict";n.d(t,{Z:()=>c});n(667294);var o=n(294184),r=n.n(o),a=n(751995),i=n(49937),l=n(211965);const s=a.iK.div`
  z-index: 99;
  width: 50px;
  height: unset;
  position: relative;
  display: inline-block;
  margin: 10px;
  &.inline {
    margin: 0px;
    width: 30px;
  }
  &.inline-centered {
    margin: 0 auto;
    width: 30px;
    display: block;
  }
  &.floating {
    padding: 0;
    margin: 0;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
`;function c({position:e="floating",className:t,size:n,tip:o="",style:a={}}){return(0,l.tZ)(s,{className:r()("loading",e,t),"aria-live":"polite","aria-label":"Loading","data-test":"loading-indicator",style:a},(0,l.tZ)(i.yC,{size:n||("floating"===e?"large":"default"),tip:o}))}},672570:(e,t,n)=>{"use strict";n.d(t,{Dz:()=>g,Gb:()=>p,K7:()=>s,RS:()=>c,bM:()=>d,fz:()=>l,h:()=>i,s2:()=>h,ws:()=>u});var o=n(714670),r=n.n(o),a=n(101927);const i="ADD_TOAST";function l({toastType:e,text:t,duration:n=8e3,noDuplicate:o=!1}){return{type:i,payload:{id:(a=e,`${a}-${r().generate()}`),toastType:e,text:t,duration:n,noDuplicate:o}};var a}const s="REMOVE_TOAST";function c(e){return{type:s,payload:{id:e}}}function d(e,t){return l({text:e,toastType:a.p.INFO,duration:4e3,...t})}function u(e,t){return l({text:e,toastType:a.p.SUCCESS,duration:4e3,...t})}function g(e,t){return l({text:e,toastType:a.p.WARNING,duration:6e3,...t})}function p(e,t){return l({text:e,toastType:a.p.DANGER,duration:8e3,...t})}const h={addInfoToast:d,addSuccessToast:u,addWarningToast:g,addDangerToast:p}},101927:(e,t,n)=>{"use strict";var o;n.d(t,{p:()=>o}),function(e){e.INFO="INFO_TOAST",e.SUCCESS="SUCCESS_TOAST",e.WARNING="WARNING_TOAST",e.DANGER="DANGER_TOAST"}(o||(o={}))},414114:(e,t,n)=>{"use strict";n.d(t,{ZP:()=>s,e1:()=>c});var o=n(667294),r=n(14890),a=n(828216),i=n(672570);const l={addInfoToast:i.bM,addSuccessToast:i.ws,addWarningToast:i.Dz,addDangerToast:i.Gb};function s(e){return(0,a.$j)(((e,t)=>({...e,...t})),(e=>(0,r.DE)(l,e)))(e)}function c(){const e=(0,a.I0)();return(0,o.useMemo)((()=>(0,r.DE)(l,e)),[e])}},774069:(e,t,n)=>{"use strict";n.d(t,{o:()=>f,Z:()=>R});var o=n(205872),r=n.n(o),a=n(414293),i=n.n(a),l=n(667294),s=n(751995),c=n(455867),d=n(211965),u=n(49937),g=n(835932),p=n(929119),h=n(861193),v=n.n(h);const f=(0,s.iK)((e=>(0,d.tZ)(u.xT,r()({},e,{maskTransitionName:""}))))`
  ${({theme:e,responsive:t,maxWidth:n})=>t&&(0,d.iv)("max-width:",null!=n?n:"900px",";padding-left:",3*e.gridUnit,"px;padding-right:",3*e.gridUnit,"px;padding-bottom:0;top:0;","")}

  .ant-modal-content {
    display: flex;
    flex-direction: column;
    max-height: ${({theme:e})=>`calc(100vh - ${8*e.gridUnit}px)`};
    margin-bottom: ${({theme:e})=>4*e.gridUnit}px;
    margin-top: ${({theme:e})=>4*e.gridUnit}px;
  }

  .ant-modal-header {
    flex: 0 0 auto;
    background-color: ${({theme:e})=>e.colors.grayscale.light4};
    border-radius: ${({theme:e})=>e.borderRadius}px
      ${({theme:e})=>e.borderRadius}px 0 0;
    padding-left: ${({theme:e})=>4*e.gridUnit}px;
    padding-right: ${({theme:e})=>4*e.gridUnit}px;

    .ant-modal-title h4 {
      display: flex;
      margin: 0;
      align-items: center;
    }
  }

  .ant-modal-close-x {
    display: flex;
    align-items: center;

    .close {
      flex: 1 1 auto;
      margin-bottom: ${({theme:e})=>e.gridUnit}px;
      color: ${({theme:e})=>e.colors.secondary.dark1};
      font-size: 32px;
      font-weight: ${({theme:e})=>e.typography.weights.light};
    }
  }

  .ant-modal-body {
    flex: 0 1 auto;
    padding: ${({theme:e})=>4*e.gridUnit}px;
    overflow: auto;
    ${({resizable:e,height:t})=>!e&&t&&`height: ${t};`}
  }
  .ant-modal-footer {
    flex: 0 0 1;
    border-top: ${({theme:e})=>e.gridUnit/4}px solid
      ${({theme:e})=>e.colors.grayscale.light2};
    padding: ${({theme:e})=>4*e.gridUnit}px;

    .btn {
      font-size: 12px;
      text-transform: uppercase;
    }

    .btn + .btn {
      margin-left: ${({theme:e})=>2*e.gridUnit}px;
    }
  }

  // styling for Tabs component
  // Aaron note 20-11-19: this seems to be exclusively here for the Edit Database modal.
  // TODO: remove this as it is a special case.
  .ant-tabs-top {
    margin-top: -${({theme:e})=>4*e.gridUnit}px;
  }

  &.no-content-padding .ant-modal-body {
    padding: 0;
  }

  ${({draggable:e,theme:t})=>e&&`\n    .ant-modal-header {\n      padding: 0;\n      .draggable-trigger {\n          cursor: move;\n          padding: ${4*t.gridUnit}px;\n          width: 100%;\n        }\n    }\n  `};

  ${({resizable:e,hideFooter:t})=>e&&`\n    .resizable {\n      pointer-events: all;\n\n      .resizable-wrapper {\n        height: 100%;\n      }\n\n      .ant-modal-content {\n        height: 100%;\n\n        .ant-modal-body {\n          /* 100% - header height - footer height */\n          height: ${t?"calc(100% - 55px);":"calc(100% - 55px - 65px);"}\n        }\n      }\n    }\n  `}
`,m=e=>({maxHeight:"100vh",maxWidth:"100vw",minHeight:e?109:174,minWidth:"380px",enable:{bottom:!0,bottomLeft:!1,bottomRight:!0,left:!1,top:!1,topLeft:!1,topRight:!1,right:!0}}),_=({children:e,disablePrimaryButton:t=!1,primaryButtonLoading:n=!1,onHide:o,onHandledPrimaryAction:a,primaryButtonName:s=(0,c.t)("OK"),primaryButtonType:u="primary",show:h,name:_,title:b,width:R,maxWidth:E,responsive:O=!1,centered:N,footer:C,hideFooter:S,wrapProps:y,draggable:x=!1,resizable:T=!1,resizableConfig:w=m(S),draggableConfig:Z,destroyOnClose:A,...I})=>{const $=(0,l.useRef)(null),[k,D]=(0,l.useState)(),[P,U]=(0,l.useState)(!0);let L;l.isValidElement(C)&&(L=l.cloneElement(C,{closeModal:o}));const M=i()(L)?[(0,d.tZ)(g.Z,{key:"back",onClick:o,cta:!0,"data-test":"modal-cancel-button"},(0,c.t)("Cancel")),(0,d.tZ)(g.Z,{key:"submit",buttonStyle:u,disabled:t,loading:n,onClick:a,cta:!0,"data-test":"modal-confirm-button"},s)]:L,z=R||(O?"100vw":"600px"),W=!(T||x),F=(0,l.useMemo)((()=>0===Object.keys(w).length?m(S):w),[S,w]);return(0,d.tZ)(f,r()({centered:!!N,onOk:a,onCancel:o,width:z,maxWidth:E,responsive:O,visible:h,title:(0,d.tZ)((()=>x?(0,d.tZ)("div",{className:"draggable-trigger",onMouseOver:()=>P&&U(!1),onMouseOut:()=>!P&&U(!0)},b):(0,d.tZ)(l.Fragment,null,b)),null),closeIcon:(0,d.tZ)("span",{className:"close","aria-hidden":"true"},"\xd7"),footer:S?null:M,hideFooter:S,wrapProps:{"data-test":`${_||b}-modal`,...y},modalRender:e=>T||x?(0,d.tZ)(v(),r()({disabled:!x||P,bounds:k,onStart:(e,t)=>((e,t)=>{var n,o,r;const{clientWidth:a,clientHeight:i}=null==(n=window)||null==(o=n.document)?void 0:o.documentElement,l=null==$||null==(r=$.current)?void 0:r.getBoundingClientRect();l&&D({left:-(null==l?void 0:l.left)+(null==t?void 0:t.x),right:a-((null==l?void 0:l.right)-(null==t?void 0:t.x)),top:-(null==l?void 0:l.top)+(null==t?void 0:t.y),bottom:i-((null==l?void 0:l.bottom)-(null==t?void 0:t.y))})})(0,t)},Z),T?(0,d.tZ)(p.e,r()({className:"resizable"},F),(0,d.tZ)("div",{className:"resizable-wrapper",ref:$},e)):(0,d.tZ)("div",{ref:$},e)):e,mask:W,draggable:x,resizable:T,destroyOnClose:A},I),e)};_.displayName="Modal";const b={okButtonProps:{className:"modal-functions-ok-button"},cancelButtonProps:{className:"modal-functions-cancel-button"}},R=Object.assign(_,{error:e=>u.xT.error({...e,...b}),warning:e=>u.xT.warning({...e,...b}),confirm:e=>u.xT.confirm({...e,...b}),useModal:u.xT.useModal})},784101:(e,t,n)=>{"use strict";n.d(t,{Z:()=>O});var o=n(205872),r=n.n(o),a=n(618446),i=n.n(a),l=n(667294),s=n(455867),c=n(355786),d=n(23279),u=n.n(d),g=n(731293),p=n(998286),h=n(427600),v=n(985633),f=n(747767),m=n(163542),_=n(134891),b=n(211965);const R=({error:e})=>(0,b.tZ)(f.BD,null,(0,b.tZ)(g.Z.ErrorSolid,null)," ",(0,b.tZ)(f.Vv,null,e)),E=(e,t,n)=>`${e};${t};${n}`,O=(0,l.forwardRef)((({allowClear:e,allowNewOptions:t=!1,ariaLabel:n,fetchOnlyOnSearch:o,filterOption:a=!0,header:d=null,headerPosition:g="top",helperText:O,invertSelection:N=!1,lazyLoading:C=!0,loading:S,mode:y="single",name:x,notFoundContent:T,onError:w,onChange:Z,onClear:A,onDropdownVisibleChange:I,optionFilterProps:$=["label","value"],options:k,pageSize:D=m.L8,placeholder:P=(0,s.t)("Select ..."),showSearch:U=!0,sortComparator:L=m.Ns,tokenSeparators:M,value:z,getPopupContainer:W,oneLine:F,maxTagCount:q,...K},B)=>{const G="single"===y,[V,Y]=(0,l.useState)(z),[j,H]=(0,l.useState)(""),[Q,X]=(0,l.useState)(S),[J,ee]=(0,l.useState)(""),[te,ne]=(0,l.useState)(!1),[oe,re]=(0,l.useState)(0),[ae,ie]=(0,l.useState)(0),[le,se]=(0,l.useState)(!C),[ce,de]=(0,l.useState)(!1),ue=(0,l.useRef)(V),ge=(0,l.useRef)(new Map),pe=G?void 0:t?"tags":"multiple",he=!o||j,[ve,fe]=(0,l.useState)(null!=q?q:m.pM);(0,l.useEffect)((()=>{F&&fe(te?0:1)}),[te,F]),(0,l.useEffect)((()=>{ue.current=V}),[V]);const me=(0,l.useCallback)(((e,t)=>(0,v.Y1)(e,t,ue.current)),[]),_e=(0,l.useCallback)(((e,t)=>(0,v.tj)(e,t,j,me,L)),[j,L,me]),be=(0,l.useCallback)(((e,t)=>(0,v.Sl)(e,t,me,L)),[L,me]),[Re,Ee]=(0,l.useState)(m.DW),Oe=(0,l.useMemo)((()=>{const e=(0,c.Z)(V).filter((e=>!(0,v.Gq)((0,v.NA)(e),Re))).map((e=>(0,v.nq)(e)?e:{value:e,label:String(e)}));return e.length>0?e.concat(Re):Re}),[Re,V]),Ne=(0,l.useCallback)((e=>(0,p.O$)(e).then((e=>{const{error:t}=e;ee(t),w&&w(t)}))),[w]),Ce=(0,l.useCallback)((e=>{let t=[];if(e&&Array.isArray(e)&&e.length){const n=new Set(e.map((e=>e.value)));Ee((o=>(t=o.filter((e=>!n.has(e.value))).concat(e).sort(be),t)))}return t}),[be]),Se=(0,l.useMemo)((()=>(e,t)=>{if(re(t),ce)return void X(!1);const n=E(e,t,D),r=ge.current.get(n);if(void 0!==r)return ie(r),void X(!1);X(!0);k(e,t,D).then((({data:t,totalCount:r})=>{const a=Ce(t);ge.current.set(n,r),ie(r),!o&&""===e&&a.length>=r&&de(!0)})).catch(Ne).finally((()=>{X(!1)}))}),[ce,o,Ce,Ne,k,D]),ye=(0,l.useMemo)((()=>u()(Se,h.M$)),[Se]);(0,l.useEffect)((()=>{ge.current.clear(),de(!1),Ee(m.DW)}),[k]),(0,l.useEffect)((()=>{Y(z)}),[z]),(0,l.useEffect)((()=>()=>{ye.cancel()}),[ye]),(0,l.useEffect)((()=>{le&&he&&(j?ye(j,0):Se("",0))}),[le,Se,he,j,ye]),(0,l.useEffect)((()=>{void 0!==S&&S!==Q&&X(S)}),[Q,S]);const xe=()=>ge.current.clear();return(0,l.useImperativeHandle)(B,(()=>({...B.current,clearCache:xe})),[B]),(0,b.tZ)(f.PQ,{headerPosition:g},d&&(0,b.tZ)(f.eb,{headerPosition:g},d),(0,b.tZ)(f.Qr,r()({allowClear:!Q&&e,"aria-label":n||x,dropdownRender:e=>(0,v.RI)(e,te,Q,Oe.length,O,J?(0,b.tZ)(R,{error:J}):void 0),filterOption:(e,t)=>(0,v.Dz)(e,t,$,a),filterSort:_e,getPopupContainer:W||(e=>e.parentNode),headerPosition:g,labelInValue:!0,maxTagCount:ve,mode:pe,notFoundContent:Q?(0,s.t)("Loading..."):T,onDeselect:e=>{if(Array.isArray(V))if((0,v.nq)(e)){Y(V.filter((t=>t.value!==e.value)))}else{Y(V.filter((t=>t!==e)))}H("")},onDropdownVisibleChange:e=>{if(ne(e),le!==e&&se(e),!e&&Q&&setTimeout((()=>{X(!1)}),250),e&&!j&&Re.length>1){const e=Re.slice().sort(be);i()(e,Re)||Ee(e)}I&&I(e)},onPopupScroll:e=>{const t=e.currentTarget,n=t.scrollTop>.7*(t.scrollHeight-t.offsetHeight);if(!Q&&oe*D+D<ae&&n){Se(j,oe+1)}},onSearch:U?e=>{const n=e.trim();if(t&&G){const e=n&&!(0,v.Gq)(n,Oe,!0)&&{label:n,value:n,isNewOption:!0},t=Oe.filter((e=>!e.isNewOption||(0,v.Gq)(e.value,V))),o=e?[e,...t]:t;Ee(o)}ce||!le||ge.current.has(E(n,0,D))||X(!(o&&!n)),H(e)}:void 0,onSelect:e=>{Y(G?e:t=>{const n=(0,c.Z)(t),o=(0,v.NA)(e);if(!(0,v.Gq)(o,n)){const t=[...n,e];return(0,v.nq)(e),t}return t}),H("")},onClear:()=>{Y(void 0),A&&A()},onChange:Z,options:(0,v.$)(Oe)?void 0:Oe,placeholder:P,showSearch:U,showArrow:!0,tokenSeparators:M||m.pp,value:V,suffixIcon:(0,v.AI)(Q,U,te),menuItemSelectedIcon:N?(0,b.tZ)(f.F6,{iconSize:"m","aria-label":"stop"}):(0,b.tZ)(f.Y1,{iconSize:"m","aria-label":"check"}),oneLine:F,tagRender:_.Z},K,{ref:B}),(0,v.$)(Oe)&&(0,v.PO)(Oe)))}))},134891:(e,t,n)=>{"use strict";n.d(t,{Z:()=>h});var o=n(205872),r=n.n(o),a=(n(667294),n(560331)),i=n(751995),l=n(763279),s=n(358593),c=n(985633),d=n(747767),u=n(211965);const g=(0,i.iK)(a.Z)`
  & .ant-tag-close-icon {
    display: inline-flex;
    align-items: center;
    margin-left: ${({theme:e})=>e.gridUnit}px;
  }

  & .tag-content {
    overflow: hidden;
    text-overflow: ellipsis;
  }
`,p=e=>{const[t,n]=(0,l.cB)();return(0,u.tZ)(s.u,{title:n?e.children:null},(0,u.tZ)(g,r()({},e,{className:"ant-select-selection-item"}),(0,u.tZ)("span",{className:"tag-content",ref:t},e.children)))},h=e=>{const{label:t,value:n}=e,o=e=>{const t=e.target;("svg"===t.tagName||"path"===t.tagName||"span"===t.tagName&&t.className.includes("ant-tag-close-icon"))&&e.stopPropagation()};return n!==c.qP?(0,u.tZ)(p,r()({onMouseDown:o},e),t):(0,u.tZ)(d.WC,null)}},281315:(e,t,n)=>{"use strict";n.d(t,{Z:()=>R});var o=n(205872),r=n.n(o),a=n(23279),i=n.n(a),l=n(618446),s=n.n(l),c=n(667294),d=n(455867),u=n(355786),g=n(767190),p=n(645636),h=n(564749),v=n(985633),f=n(747767),m=n(163542),_=n(134891),b=n(211965);const R=(0,c.forwardRef)((({allowClear:e,allowNewOptions:t=!1,ariaLabel:n,filterOption:o=!0,header:a=null,headerPosition:l="top",helperText:R,invertSelection:E=!1,labelInValue:O=!1,loading:N,mode:C="single",name:S,notFoundContent:y,onChange:x,onClear:T,onDropdownVisibleChange:w,optionFilterProps:Z=["label","value"],options:A,placeholder:I=(0,d.t)("Select ..."),showSearch:$=!0,sortComparator:k=m.Ns,tokenSeparators:D,value:P,getPopupContainer:U,oneLine:L,maxTagCount:M,...z},W)=>{const F="single"===C,q=!!t||$,[K,B]=(0,c.useState)(P),[G,V]=(0,c.useState)(""),[Y,j]=(0,c.useState)(N),[H,Q]=(0,c.useState)(!1),[X,J]=(0,c.useState)(null!=M?M:m.pM);(0,c.useEffect)((()=>{L&&J(H?0:1)}),[H,L]);const ee=F?void 0:t?"tags":"multiple",{Option:te}=h.Z,ne=(0,c.useCallback)(((e,t)=>(0,v.Y1)(e,t,K)),[K]),oe=(0,c.useCallback)(((e,t)=>(0,v.tj)(e,t,G,ne,k)),[G,k,ne]),re=(0,c.useMemo)((()=>A&&Array.isArray(A)?A.slice():m.DW),[A]),ae=(0,c.useMemo)((()=>re.slice().sort(ne)),[re,ne]),[ie,le]=(0,c.useState)(ae),se=(0,c.useMemo)((()=>{const e=(0,u.Z)(K).filter((e=>!(0,v.Gq)((0,v.NA)(e),ie))).map((e=>(0,v.nq)(e)?e:{value:e,label:String(e)}));return(e.length>0?e.concat(ie):ie).filter((e=>e.value!==v.qP))}),[ie,K]),ce=(0,c.useMemo)((()=>se.filter((e=>!e.disabled))),[se]),de=(0,c.useMemo)((()=>se.filter((e=>(0,v.Gq)(e.value,K)||!e.disabled))),[se,K]),ue=(0,c.useMemo)((()=>!F&&ie.length>0&&ce.length>1&&!G),[F,ie.length,ce.length,G]),ge=(0,c.useMemo)((()=>(0,u.Z)(K).length===de.length+1),[K,de]),pe=()=>{B(se.filter((e=>e.disabled&&(0,v.Gq)(e.value,K))).map((e=>O?{label:e.label,value:e.value}:e.value)))};(0,c.useEffect)((()=>{le(re)}),[re]),(0,c.useEffect)((()=>{void 0!==N&&N!==Y&&j(N)}),[Y,N]),(0,c.useEffect)((()=>{B(P)}),[P]);const he=(0,c.useCallback)(i()((e=>{var t;"dashbord-page-scroll"===e.data.type&&(null==W||null==(t=W.current)||t.blur())}),20),[]);(0,c.useEffect)((()=>(window.addEventListener("message",he),()=>{window.removeEventListener("message",he)})),[]),(0,c.useEffect)((()=>{!F&&(0,u.Z)(P).length===de.length&&ie.length>0&&B(O?[...(0,u.Z)(P),v.tP]:[...(0,u.Z)(P),v.qP])}),[P,F,O,de.length,ie.length]),(0,c.useEffect)((()=>{if((0,u.Z)(K).some((e=>(0,v.NA)(e)===v.qP))&&!ge){const e=de.map((e=>O?e:e.value));e.push(O?v.tP:v.qP),B(e)}}),[K,ge,O,de]);const ve=(0,c.useMemo)((()=>()=>`${v.qP} (${(0,g.uf)(p.Z.INTEGER,de.length)})`),[de]);return(0,b.tZ)(f.PQ,{headerPosition:l},a&&(0,b.tZ)(f.eb,{headerPosition:l},a),(0,b.tZ)(f.Qr,r()({allowClear:!Y&&e,"aria-label":n||S,dropdownRender:e=>(0,v.RI)(e,H,Y,se.length,R),filterOption:(e,t)=>(0,v.Dz)(e,t,Z,o),filterSort:oe,getPopupContainer:U||(e=>e.parentNode),headerPosition:l,labelInValue:O,maxTagCount:X,maxTagPlaceholder:()=>{const e=(0,u.Z)(K).length;return ge?`+ ${e-X-1} ...`:`+ ${e-X} ...`},mode:ee,notFoundContent:Y?(0,d.t)("Loading..."):y,onDeselect:e=>{if(Array.isArray(K))if((0,v.NA)(e)===(0,v.NA)(v.qP))pe();else{let t=K;t=t.filter((t=>(0,v.NA)(t)!==(0,v.NA)(e))),ge&&ie.some((t=>t.value===(0,v.NA)(e)))&&(t=t.filter((e=>(0,v.NA)(e)!==v.qP))),B(t)}V("")},onDropdownVisibleChange:e=>{Q(e),e&&!G&&ie.length>1&&(s()(ae,ie)||le(ae)),w&&w(e)},onPopupScroll:void 0,onSearch:q?e=>{const n=e.trim();if(t&&F){const e=n&&!(0,v.Gq)(n,se,!0)&&{label:n,value:n,isNewOption:!0},t=(0,u.Z)(se).filter((e=>!e.isNewOption||(0,v.Gq)(e.value,K))),o=e?[e,...t]:t;le(o)}V(e)}:void 0,onSelect:e=>{B(F?e:t=>{const n=(0,u.Z)(t),o=(0,v.NA)(e);if(o===(0,v.NA)(v.qP))return(0,v.nq)(e)?[...de,v.tP]:[v.qP,...de.map((e=>e.value))];if(!(0,v.Gq)(o,n)){const t=[...n,e];return t.length===de.length&&ue?(0,v.nq)(e)?[...t,v.tP]:[...t,v.qP]:t}return t}),V("")},onClear:()=>{pe(),T&&T()},onChange:(e,t)=>{let n=e,o=t;if(!F)if((0,u.Z)(n).some((e=>(0,v.NA)(e)===v.qP)))ge?n=(0,u.Z)(e).filter((e=>(0,v.NA)(e)!==v.qP)):(n=(0,v.Q8)(de,O),o=(0,v.vi)(de));else if((0,u.Z)(e).length===de.length&&ge){const e=de.filter((e=>(0,v.Gq)(e.value,K)&&e.disabled));n=(0,v.Q8)(e,O),o=(0,v.vi)(e)}null==x||x(n,o)},placeholder:I,showSearch:q,showArrow:!0,tokenSeparators:D||m.pp,value:K,suffixIcon:(0,v.AI)(Y,q,H),menuItemSelectedIcon:E?(0,b.tZ)(f.F6,{iconSize:"m","aria-label":"stop"}):(0,b.tZ)(f.Y1,{iconSize:"m","aria-label":"check"}),oneLine:L,tagRender:_.Z},z,{ref:W}),ue&&(0,b.tZ)(te,{id:"select-all",className:"select-all",key:v.qP,value:v.qP},ve()),(0,v.PO)(se)))}))},163542:(e,t,n)=>{"use strict";n.d(t,{DW:()=>i,L8:()=>l,Ns:()=>s,pM:()=>r,pp:()=>a});var o=n(317641);const r=4,a=[",","\r\n","\n","\t",";"],i=[],l=100,s=(e,t,n)=>{let r,a;return"string"===typeof e.label&&"string"===typeof t.label?(r=e.label,a=t.label):"string"===typeof e.value&&"string"===typeof t.value&&(r=e.value,a=t.value),"string"===typeof r&&"string"===typeof a?n?(0,o.T)(r,a,n):r.localeCompare(a):e.value-t.value}},747767:(e,t,n)=>{"use strict";n.d(t,{BD:()=>m,F6:()=>g,H$:()=>h,PQ:()=>c,Qr:()=>d,SC:()=>v,Vv:()=>_,WC:()=>u,Y1:()=>p,eb:()=>s,oz:()=>f});var o=n(751995),r=n(731293),a=n(560331),i=n(911382),l=n(564749);const s=o.iK.span`
  ${({theme:e,headerPosition:t})=>`\n    overflow: hidden;\n    text-overflow: ellipsis;\n    white-space: nowrap;\n    margin-right: ${"left"===t?2*e.gridUnit:0}px;\n  `}
`,c=o.iK.div`
  ${({headerPosition:e})=>`\n    display: flex;\n    flex-direction: ${"top"===e?"column":"row"};\n    align-items: ${"left"===e?"center":void 0};\n    width: 100%;\n  `}
`,d=(0,o.iK)(l.Z,{shouldForwardProp:e=>"headerPosition"!==e&&"oneLine"!==e})`
  ${({theme:e,headerPosition:t,oneLine:n})=>`\n    flex: ${"left"===t?1:0};\n    && .ant-select-selector {\n      border-radius: ${e.gridUnit}px;\n    }\n    // Open the dropdown when clicking on the suffix\n    // This is fixed in version 4.16\n    .ant-select-arrow .anticon:not(.ant-select-suffix) {\n      pointer-events: none;\n    }\n    .select-all {\n      border-bottom: 1px solid ${e.colors.grayscale.light3};\n    }\n    ${n&&`\n        .ant-select-selection-overflow {\n          flex-wrap: nowrap;\n        }\n\n        .ant-select-selection-overflow-item:not(.ant-select-selection-overflow-item-rest):not(.ant-select-selection-overflow-item-suffix) {\n          flex-shrink: 1;\n          min-width: ${13*e.gridUnit}px;\n        }\n\n        .ant-select-selection-overflow-item-suffix {\n          flex: unset;\n          min-width: 0px;\n        }\n      `};\n `}
`,u=o.iK.span`
  display: none;
`,g=((0,o.iK)(a.Z)`
  ${({theme:e})=>`\n    background: ${e.colors.grayscale.light3};\n    font-size: ${e.typography.sizes.m}px;\n    border: none;\n  `}
`,(0,o.iK)(r.Z.StopOutlined)`
  vertical-align: 0;
`),p=(0,o.iK)(r.Z.CheckOutlined)`
  vertical-align: 0;
`,h=(0,o.iK)(i.Z)`
  margin-top: ${({theme:e})=>-e.gridUnit}px;
`,v=o.iK.div`
  ${({theme:e})=>`\n   margin-left: ${3*e.gridUnit}px;\n   line-height: ${8*e.gridUnit}px;\n   color: ${e.colors.grayscale.light1};\n `}
`,f=o.iK.div`
  ${({theme:e})=>`\n   padding: ${2*e.gridUnit}px ${3*e.gridUnit}px;\n   color: ${e.colors.grayscale.base};\n   font-size: ${e.typography.sizes.s}px;\n   cursor: default;\n   border-bottom: 1px solid ${e.colors.grayscale.light2};\n `}
`,m=o.iK.div`
  ${({theme:e})=>`\n    display: flex;\n    justify-content: center;\n    align-items: flex-start;\n    width: 100%;\n    padding: ${2*e.gridUnit}px;\n    color: ${e.colors.error.base};\n    & svg {\n      margin-right: ${2*e.gridUnit}px;\n    }\n  `}
`,_=o.iK.div`
  overflow: hidden;
  text-overflow: ellipsis;
`},985633:(e,t,n)=>{"use strict";n.d(t,{$:()=>y,AI:()=>N,Dz:()=>S,Gq:()=>_,NA:()=>m,PO:()=>x,Q8:()=>T,RI:()=>C,Sl:()=>O,Y1:()=>R,mj:()=>b,nq:()=>f,qP:()=>p,tP:()=>h,tj:()=>E,vi:()=>w});var o=n(205872),r=n.n(o),a=n(355786),i=n(455867),l=n(564749),s=n(667294),c=n(731293),d=n(747767),u=n(211965);const{Option:g}=l.Z,p="Select All",h={value:p,label:String(p)};function v(e){return null!==e&&"object"===typeof e&&!1===Array.isArray(e)}function f(e){return v(e)&&"value"in e&&"label"in e}function m(e){return f(e)?e.value:e}function _(e,t,n=!1){return void 0!==(0,a.Z)(t).find((t=>t==e||v(t)&&("value"in t&&t.value==e||n&&"label"in t&&t.label===e)))}const b=e=>(t,n)=>"string"===typeof t[e]&&"string"===typeof n[e]?t[e].localeCompare(n[e]):t[e]-n[e],R=(e,t,n)=>n&&void 0!==e.value&&void 0!==t.value?Number(_(t.value,n))-Number(_(e.value,n)):0,E=(e,t,n,o,r)=>o(e,t)||r(e,t,n),O=(e,t,n,o)=>n(e,t)||o(e,t,""),N=(e,t,n)=>e?(0,u.tZ)(d.H$,{size:"small"}):t&&n?(0,u.tZ)(c.Z.SearchOutlined,{iconSize:"s"}):(0,u.tZ)(c.Z.DownOutlined,{iconSize:"s"}),C=(e,t,n,o,r,a)=>{var l,c;t||(null==(l=e.ref)||null==(c=l.current)||c.scrollTo({top:0}));return n&&0===o?(0,u.tZ)(d.SC,null,(0,i.t)("Loading...")):a||(0,u.tZ)(s.Fragment,null,r&&(0,u.tZ)(d.oz,{role:"note"},r),e)},S=(e,t,n,o)=>{if("function"===typeof o)return o(e,t);if(o){const o=e.trim().toLowerCase();if(null!=n&&n.length)return n.some((e=>(null!=t&&t[e]?String(t[e]).trim().toLowerCase():"").includes(o)))}return!1},y=e=>null==e?void 0:e.some((e=>!(null==e||!e.customLabel))),x=e=>e.map((e=>{const t="object"===typeof e,n=t?(null==e?void 0:e.label)||e.value:e,o=t?e.value:e,{customLabel:a,...i}=e;return(0,u.tZ)(g,r()({},i,{key:o,label:n,value:o}),t&&a?a:n)})),T=(e,t)=>t?e.map((e=>({key:e.value,value:e.value,label:e.label}))):e.map((e=>e.value)),w=e=>e.map((e=>({children:e.label,key:e.value,value:e.value,label:e.label,disabled:e.disabled})))},171262:(e,t,n)=>{"use strict";n.d(t,{Xv:()=>h,cl:()=>f,ZP:()=>m});var o=n(205872),r=n.n(o),a=(n(667294),n(211965)),i=n(751995),l=n(901350),s=n(731293);const c=({animated:e=!1,fullWidth:t=!0,allowOverflow:n=!0,...o})=>(0,a.tZ)(l.default,r()({animated:e},o,{css:e=>a.iv`
      overflow: ${n?"visible":"hidden"};

      .ant-tabs-content-holder {
        overflow: ${n?"visible":"auto"};
      }
      .ant-tabs-tab {
        flex: 1 1 auto;
        &:hover {
          .anchor-link-container {
            cursor: pointer;
            .fa.fa-link {
              visibility: visible;
            }
          }
        }
        .short-link-trigger.btn {
          padding: 0 ${e.gridUnit}px;
          & > .fa.fa-link {
            top: 0;
          }
        }
      }
      ${t&&a.iv`
        .ant-tabs-nav-list {
          width: 100%;
        }
      `};

      .ant-tabs-tab-btn {
        display: flex;
        flex: 1 1 auto;
        align-items: center;
        justify-content: center;
        font-size: ${e.typography.sizes.s}px;
        text-align: center;
        text-transform: uppercase;
        user-select: none;
        .required {
          margin-left: ${e.gridUnit/2}px;
          color: ${e.colors.error.base};
        }
      }
    `})),d=(0,i.iK)(l.default.TabPane)``,u=Object.assign(c,{TabPane:d}),g=(0,i.iK)(c)`
  ${({theme:e,fullWidth:t})=>`\n    .ant-tabs-content-holder {\n      background: ${e.colors.grayscale.light5};\n    }\n\n    & > .ant-tabs-nav {\n      margin-bottom: 0;\n    }\n\n    .ant-tabs-tab-remove {\n      padding-top: 0;\n      padding-bottom: 0;\n      height: ${6*e.gridUnit}px;\n    }\n\n    ${t?a.iv`
            .ant-tabs-nav-list {
              width: 100%;
            }
          `:""}\n  `}
`,p=(0,i.iK)(s.Z.CancelX)`
  color: ${({theme:e})=>e.colors.grayscale.base};
`,h=Object.assign(g,{TabPane:d});h.defaultProps={type:"editable-card",fullWidth:!1,animated:{inkBar:!0,tabPane:!1}},h.TabPane.defaultProps={closeIcon:(0,a.tZ)(p,{role:"button",tabIndex:0})};const v=(0,i.iK)(h)`
  &.ant-tabs-card > .ant-tabs-nav .ant-tabs-tab {
    margin: 0 ${({theme:e})=>4*e.gridUnit}px;
    padding: ${({theme:e})=>`${3*e.gridUnit}px ${e.gridUnit}px`};
    background: transparent;
    border: none;
  }

  &.ant-tabs-card > .ant-tabs-nav .ant-tabs-ink-bar {
    visibility: visible;
  }

  .ant-tabs-tab-btn {
    font-size: ${({theme:e})=>e.typography.sizes.m}px;
  }

  .ant-tabs-tab-remove {
    margin-left: 0;
    padding-right: 0;
  }

  .ant-tabs-nav-add {
    min-width: unset !important;
    background: transparent !important;
    border: none !important;
  }
`,f=Object.assign(v,{TabPane:d}),m=u},358593:(e,t,n)=>{"use strict";n.d(t,{u:()=>c});var o=n(205872),r=n.n(o),a=n(667294),i=n(751995),l=n(211965),s=n(931097);const c=e=>{const t=(0,i.Fg)();return(0,l.tZ)(a.Fragment,null,(0,l.tZ)(l.xB,{styles:l.iv`
          .ant-tooltip-open {
            display: inline-block;
            &::after {
              content: '';
              display: block;
            }
          }
        `}),(0,l.tZ)(s.Z,r()({overlayStyle:{fontSize:t.typography.sizes.s,lineHeight:"1.6"},color:`${t.colors.grayscale.dark2}e6`},e)))}},49937:(e,t,n)=>{"use strict";n.d(t,{O5:()=>re.Z,C0:()=>B.Z,Ak:()=>G.Z,r4:()=>V.Z,Ol:()=>Y.Z,Gj:()=>j.Z,qz:()=>H.Z,oc:()=>Q.Z,xT:()=>X.Z,IZ:()=>J.Z,rb:()=>ee.Z,KU:()=>te.Z,D6:()=>ne.Z,_e:()=>oe.Z,qb:()=>A.Z,qE:()=>I.C,JX:()=>$.Z,iz:()=>k.Z,HY:()=>D.Z,rj:()=>P.ZP,aV:()=>U.ZP,X2:()=>L.Z,Ph:()=>o.Z,Od:()=>M.Z,T:()=>z.Z,yC:()=>h.Z,Rg:()=>W.Z,Vp:()=>p.Z,mp:()=>F.Z,r_:()=>Z,ZT:()=>q.Z,gq:()=>K.Z});var o=n(281315),r=(n(618446),n(667294)),a=n(455867),i=n(355786),l=n(767190),s=n(645636),c=n(970553),d=(n(205872),n(564749)),u=n(731293),g=n(751995),p=n(560331),h=n(911382);const v=g.iK.span`
  ${({theme:e,headerPosition:t})=>`\n    overflow: hidden;\n    text-overflow: ellipsis;\n    white-space: nowrap;\n    margin-right: ${"left"===t?2*e.gridUnit:0}px;\n  `}
`,f=g.iK.div`
  ${({headerPosition:e})=>`\n    display: flex;\n    flex-direction: ${"top"===e?"column":"row"};\n    align-items: ${"left"===e?"center":void 0};\n    width: 100%;\n  `}
`,m=((0,g.iK)(d.Z,{shouldForwardProp:e=>"headerPosition"!==e&&"oneLine"!==e})`
  ${({theme:e,headerPosition:t,oneLine:n})=>`\n    flex: ${"left"===t?1:0};\n    && .ant-select-selector {\n      border-radius: ${e.gridUnit}px;\n    }\n    // Open the dropdown when clicking on the suffix\n    // This is fixed in version 4.16\n    .ant-select-arrow .anticon:not(.ant-select-suffix) {\n      pointer-events: none;\n    }\n    .select-all {\n      border-bottom: 1px solid ${e.colors.grayscale.light3};\n    }\n    ${n&&`\n        .ant-select-selection-overflow {\n          flex-wrap: nowrap;\n        }\n\n        .ant-select-selection-overflow-item:not(.ant-select-selection-overflow-item-rest):not(.ant-select-selection-overflow-item-suffix) {\n          flex-shrink: 1;\n          min-width: ${13*e.gridUnit}px;\n        }\n\n        .ant-select-selection-overflow-item-suffix {\n          flex: unset;\n          min-width: 0px;\n        }\n      `};\n `}
`,g.iK.span`
  display: none;
`,(0,g.iK)(p.Z)`
  ${({theme:e})=>`\n    background: ${e.colors.grayscale.light3};\n    font-size: ${e.typography.sizes.m}px;\n    border: none;\n  `}
`,(0,g.iK)(u.Z.StopOutlined)`
  vertical-align: 0;
`,(0,g.iK)(u.Z.CheckOutlined)`
  vertical-align: 0;
`,(0,g.iK)(h.Z)`
  margin-top: ${({theme:e})=>-e.gridUnit}px;
`,g.iK.div`
  ${({theme:e})=>`\n   margin-left: ${3*e.gridUnit}px;\n   line-height: ${8*e.gridUnit}px;\n   color: ${e.colors.grayscale.light1};\n `}
`),_=g.iK.div`
  ${({theme:e})=>`\n   padding: ${2*e.gridUnit}px ${3*e.gridUnit}px;\n   color: ${e.colors.grayscale.base};\n   font-size: ${e.typography.sizes.s}px;\n   cursor: default;\n   border-bottom: 1px solid ${e.colors.grayscale.light2};\n `}
`;g.iK.div`
  ${({theme:e})=>`\n    display: flex;\n    justify-content: center;\n    align-items: flex-start;\n    width: 100%;\n    padding: ${2*e.gridUnit}px;\n    color: ${e.colors.error.base};\n    & svg {\n      margin-right: ${2*e.gridUnit}px;\n    }\n  `}
`,g.iK.div`
  overflow: hidden;
  text-overflow: ellipsis;
`;var b=n(211965);const{Option:R}=d.Z,E="Select All",O={value:E,label:String(E)};function N(e){return null!==e&&"object"===typeof e&&!1===Array.isArray(e)}function C(e){return N(e)&&"value"in e&&"label"in e}function S(e){return C(e)?e.value:e}function y(e,t,n=!1){return void 0!==(0,i.Z)(t).find((t=>t==e||N(t)&&("value"in t&&t.value==e||n&&"label"in t&&t.label===e)))}var x=n(317641);const T=[],w=(e,t,n)=>{let o,r;return"string"===typeof e.label&&"string"===typeof t.label?(o=e.label,r=t.label):"string"===typeof e.value&&"string"===typeof t.value&&(o=e.value,r=t.value),"string"===typeof o&&"string"===typeof r?n?(0,x.T)(o,r,n):o.localeCompare(r):e.value-t.value},Z=(0,r.forwardRef)((({allowClear:e,allowNewOptions:t=!1,ariaLabel:n,filterOption:o=!0,header:d=null,headerPosition:u="top",helperText:g,invertSelection:p=!1,labelInValue:h=!1,loading:R,mode:N="single",name:x,notFoundContent:Z,onChange:A,onClear:I,onDropdownVisibleChange:$,optionFilterProps:k=["label","value"],options:D,placeholder:P=(0,a.t)("Select ..."),showSearch:U=!0,sortComparator:L=w,tokenSeparators:M,value:z,getPopupContainer:W,oneLine:F,maxTagCount:q,...K},B)=>{const G="single"===N,[V,Y]=(0,r.useState)(z),[j,H]=(0,r.useState)(""),[Q,X]=(0,r.useState)(R),[J,ee]=(0,r.useState)(!1),[te,ne]=(0,r.useState)(null!=q?q:4);(0,r.useEffect)((()=>{F&&ne(J?0:1)}),[J,F]);const oe=(0,r.useCallback)(((e,t)=>((e,t,n)=>n&&void 0!==e.value&&void 0!==t.value?Number(y(t.value,n))-Number(y(e.value,n)):0)(e,t,V)),[V]),re=((0,r.useCallback)(((e,t)=>((e,t,n,o,r)=>o(e,t)||r(e,t,n))(e,t,j,oe,L)),[j,L,oe]),(0,r.useMemo)((()=>D&&Array.isArray(D)?D.slice():T),[D])),ae=(0,r.useMemo)((()=>re.slice().sort(oe)),[re,oe]),[ie,le]=(0,r.useState)(ae),se=(0,r.useMemo)((()=>{const e=(0,i.Z)(V).filter((e=>!y(S(e),ie))).map((e=>C(e)?e:{value:e,label:String(e)}));return(e.length>0?e.concat(ie):ie).filter((e=>e.value!==E))}),[ie,V]),ce=(0,r.useMemo)((()=>se.filter((e=>!e.disabled))),[se]),de=(0,r.useMemo)((()=>se.filter((e=>y(e.value,V)||!e.disabled))),[se,V]),ue=((0,r.useMemo)((()=>!G&&ie.length>0&&ce.length>1&&!j),[G,ie.length,ce.length,j]),(0,r.useMemo)((()=>(0,i.Z)(V).length===de.length+1),[V,de]));(0,r.useEffect)((()=>{le(re)}),[re]),(0,r.useEffect)((()=>{void 0!==R&&R!==Q&&X(R)}),[Q,R]),(0,r.useEffect)((()=>{Y(z)}),[z]),(0,r.useEffect)((()=>{!G&&(0,i.Z)(z).length===de.length&&ie.length>0&&Y(h?[...(0,i.Z)(z),O]:[...(0,i.Z)(z),E])}),[z,G,h,de.length,ie.length]),(0,r.useEffect)((()=>{if((0,i.Z)(V).some((e=>S(e)===E))&&!ue){const e=de.map((e=>h?e:e.value));e.push(h?O:E),Y(e)}}),[V,ue,h,de]);(0,r.useMemo)((()=>()=>`${E} (${(0,l.uf)(s.Z.INTEGER,de.length)})`),[de]);const ge={treeData:se,value:z,onChange:A,treeCheckable:!0,placeholder:(0,a.t)("Please select"),dropdownRender:e=>((e,t,n,o,i,l)=>{var s,c;return t||null==(s=e.ref)||null==(c=s.current)||c.scrollTo({top:0}),n&&0===o?(0,b.tZ)(m,null,(0,a.t)("Loading...")):l||(0,b.tZ)(r.Fragment,null,i&&(0,b.tZ)(_,{role:"note"},i),e)})(e,J,Q,se.length,g),style:{width:"100%"},getPopupContainer:e=>(null==e?void 0:e.triggerNode)||document.body};return(0,b.tZ)(f,{headerPosition:u},d&&(0,b.tZ)(v,{headerPosition:u},d),(0,b.tZ)(c.Z,ge))}));var A=n(784101),I=n(751890),$=n(515746),k=n(227049),D=n(814277),P=n(75302),U=n(338272),L=n(771230),M=n(133860),z=n(519650),W=n(497880),F=n(591665),q=n(216068),K=n(213958),B=n(71577),G=n(339144),V=n(609676),Y=n(427279),j=n(113013),H=n(164561),Q=n(432787),X=n(757016),J=n(734041),ee=n(231955),te=n(359314),ne=n(948205),oe=n(931097),re=n(435247)},763279:(e,t,n)=>{"use strict";n.d(t,{B3:()=>a,cB:()=>i,ro:()=>r});var o=n(667294);const r=(e,t)=>{var n,r;const[a,i]=(0,o.useState)(0),[l,s]=(0,o.useState)(!1),c=(0,o.useRef)({scrollWidth:0,parentElementWidth:0,plusRefWidth:0});return(0,o.useLayoutEffect)((()=>{var n;const o=e.current,r=null==t?void 0:t.current;if(!o)return;const{scrollWidth:a,clientWidth:l,childNodes:d}=o,u=c.current,g=(null==(n=o.parentElement)?void 0:n.clientWidth)||0,p=(null==r?void 0:r.offsetWidth)||0;if(c.current={scrollWidth:a,parentElementWidth:g,plusRefWidth:p},u.parentElementWidth!==g||u.scrollWidth!==a||u.plusRefWidth!==p)if(a>l){const e=6,t=(null==r?void 0:r.offsetWidth)||0,n=l-e,o=d.length;let a=0,c=0;for(let r=0;r<o;r+=1){n-e-a-t<=0&&(c+=1),a+=d[r].offsetWidth}o>1&&c?(s(!0),i(c)):(s(!1),i(1))}else s(!1),i(0)}),[null==(n=e.current)?void 0:n.offsetWidth,null==(r=e.current)?void 0:r.clientWidth,e]),[a,l]};const a={name:"l8l8b8",styles:"white-space:nowrap;overflow:hidden;text-overflow:ellipsis"},i=()=>{const[e,t]=(0,o.useState)(!0),n=(0,o.useRef)(null),[r,a]=(0,o.useState)(0),[i,l]=(0,o.useState)(0);return(0,o.useEffect)((()=>{var e,t,o,r;a(null!=(e=null==(t=n.current)?void 0:t.offsetWidth)?e:0),l(null!=(o=null==(r=n.current)?void 0:r.scrollWidth)?o:0)})),(0,o.useEffect)((()=>{t(r<i)}),[r,i]),[n,e]}},599543:(e,t,n)=>{"use strict";n.d(t,{E8:()=>w,JB:()=>Z,SJ:()=>E,_0:()=>y,gP:()=>C,gf:()=>N,hU:()=>T,p1:()=>S,wK:()=>O,zd:()=>x});var o=n(428368),r=n.n(o),a=n(845220),i=n.n(a),l=n(352353),s=n.n(l),c=n(957557),d=n.n(c),u=n(114176),g=n.n(u),p=n(618446),h=n.n(p),v=n(714670),f=n.n(v),m=n(14890),_=n(964417),b=n.n(_),R=n(355786);function E(e,t,n){const o={...e[t]},r={...n};return r.id||(r.id=f().generate()),o[r.id]=r,{...e,[t]:o}}function O(e,t,n,o){const r={...e[t]};return r[n.id]={...r[n.id],...o},{...e,[t]:r}}function N(e,t,n,o,r="id"){const a=[];return e[t].forEach((e=>{n[r]===e[r]?a.push({...e,...o}):a.push(e)})),{...e,[t]:a}}function C(e,t,n,o="id"){const r=[];return e[t].forEach((e=>{n[o]!==e[o]&&r.push(e)})),{...e,[t]:r}}function S(e,t){let n;return e.forEach((e=>{e.id===t&&(n=e)})),n}function y(e,t,n,o=!1){const r={...n};r.id||(r.id=f().generate());const a={};return a[t]=o?[r,...e[t]]:[...e[t],r],{...e,...a}}function x(e,t,n,o=!1){const r=[...n];r.forEach((e=>{e.id||(e.id=f().generate())}));const a={};return a[t]=o?[...r,...e[t]]:[...e[t],...r],{...e,...a}}function T(e=!0,t={},n=!1){const{paths:o,config:r}=t,a=m.qC;return e?a(b()(o,r)):a()}function w(e,t){if(!e||!t)return!1;if(e.length!==t.length)return!1;const{length:n}=e;for(let o=0;o<n;o+=1)if(e[o]!==t[o])return!1;return!0}function Z(e,t,n={ignoreUndefined:!1,ignoreNull:!1,ignoreFields:[]}){var o;let a=e,l=t;if(n.ignoreUndefined&&(a=g()(a,s()),l=g()(l,s())),n.ignoreNull&&(a=g()(a,i()),l=g()(l,i())),null!=(o=n.ignoreFields)&&o.length){const e=(0,R.Z)(n.ignoreFields);return r()(a,l,((t,n)=>h()((0,R.Z)(t).map((t=>d()(t,e))),(0,R.Z)(n).map((t=>d()(t,e))))))}return h()(a,l)}},710222:(e,t,n)=>{"use strict";n.d(t,{Z:()=>r});var o=n(454076);const r=e=>(async e=>{if((0,o.G6)())try{const t=new ClipboardItem({"text/plain":e()});await navigator.clipboard.write([t])}catch{const t=await e();await navigator.clipboard.writeText(t)}else{const t=await e();await navigator.clipboard.writeText(t)}})(e).catch((()=>e().then((e=>new Promise(((t,n)=>{const o=document.getSelection();if(o){o.removeAllRanges();const t=document.createRange(),r=document.createElement("span");r.textContent=e,r.style.position="fixed",r.style.top="0",r.style.clip="rect(0, 0, 0, 0)",r.style.whiteSpace="pre",document.body.appendChild(r),t.selectNode(r),o.addRange(t);try{document.execCommand("copy")||n()}catch(e){n()}document.body.removeChild(r),o.removeRange?o.removeRange(t):o.removeAllRanges()}t()}))))))},966785:(e,t,n)=>{"use strict";n.d(t,{Z:()=>o});const o={SESSION_TIMED_OUT:"Your session timed out, please refresh your page and try again."}},998286:(e,t,n)=>{"use strict";n.d(t,{HR:()=>l,MV:()=>i,O$:()=>s,d7:()=>c});var o=n(455867),r=n(167663),a=n(966785);function i(e){let t={...e};var n,r;t.errors&&t.errors.length>0&&(t.error=t.description=t.errors[0].message,t.link=null==(n=t.errors[0])||null==(r=n.extra)?void 0:r.link);if(!t.error&&t.message){var i;if("object"===typeof t.message)t.error=(null==(i=Object.values(t.message)[0])?void 0:i[0])||(0,o.t)("Invalid input");"string"===typeof t.message&&(t.error=t.message)}return t.stack?t={...t,error:(0,o.t)("Unexpected error: ")+(t.description||(0,o.t)("(no description, click to see stack trace)")),stacktrace:t.stack}:t.responseText&&t.responseText.indexOf("CSRF")>=0&&(t={...t,error:(0,o.t)(a.Z.SESSION_TIMED_OUT)}),{...t,error:t.error}}async function l(e,t){const{error:n,message:r}=await s(e);let a=(0,o.t)("Sorry, an unknown error occurred.");return n&&(a=(0,o.t)("Sorry, there was an error saving this %s: %s",t,n)),"string"===typeof r&&"Forbidden"===r&&(a=(0,o.t)("You do not have permission to edit this %s",t)),a}function s(e){return new Promise((t=>{if("string"===typeof e)return void t({error:e});if(e instanceof TypeError&&"Failed to fetch"===e.message)return void t({error:(0,o.t)("Network error")});if("timeout"in e&&"statusText"in e&&"timeout"===e.statusText)return void t({...e,error:(0,o.t)("Request timed out"),errors:[{error_type:r.C.FRONTEND_TIMEOUT_ERROR,extra:{timeout:e.timeout/1e3,issue_codes:[{code:1e3,message:(0,o.t)("Issue 1000 - The dataset is too large to query.")},{code:1001,message:(0,o.t)("Issue 1001 - The database is under an unusual load.")}]},level:"error",message:"Request timed out"}]});const n=e instanceof Response?e:e.response;if(n&&!n.bodyUsed)return void n.clone().json().then((e=>{const o={...n,...e};t(i(o))})).catch((()=>{n.text().then((e=>{t({...n,error:e})}))}));let a=e.statusText||e.message;a||(a=(0,o.t)("An error occurred")),t({...n,error:a})}))}function c(e,t){let n=e;const o=(null==t?void 0:t.message)||(null==t?void 0:t.error);return o&&(n=`${n}:\n${o}`),n}},317641:(e,t,n)=>{"use strict";function o(e,t,n){const o=e.toLowerCase()||"",r=t.toLowerCase()||"",a=n.toLowerCase()||"";return n&&(Number(t===n)-Number(e===n)||Number(t.startsWith(n))-Number(e.startsWith(n))||Number(r===a)-Number(o===a)||Number(r.startsWith(a))-Number(o.startsWith(a))||Number(t.includes(n))-Number(e.includes(n))||Number(r.includes(a))-Number(e.includes(a)))||e.localeCompare(t)}n.d(t,{T:()=>o})},335782:(e,t,n)=>{var o={"./alert.svg":[857249,57249],"./alert_solid.svg":[752797,52797],"./alert_solid_small.svg":[71256,71256],"./area-chart-tile.svg":[737989,37989],"./auto-resize.svg":[172630,72630],"./ballot.svg":[587760,87760],"./bar-chart-tile.svg":[443187,43187],"./big-number-chart-tile.svg":[801402,1402],"./binoculars.svg":[738970,38970],"./blank.svg":[526047,26047],"./bolt.svg":[304794,4794],"./bolt_small.svg":[49510,49510],"./bolt_small_run.svg":[336883,36883],"./calendar.svg":[265816,65816],"./cancel-x.svg":[577654,77654],"./cancel.svg":[114757,14757],"./cancel_solid.svg":[755777,55777],"./card_view.svg":[25838,25838],"./cards.svg":[581293,81293],"./cards_locked.svg":[369052,69052],"./caret_delete.svg":[798520,98520],"./caret_down.svg":[187832,87832],"./caret_edit.svg":[960692,60692],"./caret_left.svg":[180310,80310],"./caret_more.svg":[418961,18961],"./caret_right.svg":[164817,64817],"./caret_up.svg":[639811,39811],"./category.svg":[824851,24851],"./certified.svg":[88695,88695],"./chart-pcicon.svg":[846104,46104],"./chart.svg":[231454,31454],"./check.svg":[983544,83544],"./checkbox-half.svg":[457405,57405],"./checkbox-off.svg":[475281,75281],"./checkbox-on.svg":[99013,99013],"./circle.svg":[160183,60183],"./circle_check.svg":[193558,93558],"./circle_check_solid.svg":[570992,70992],"./clock.svg":[350597,50597],"./close.svg":[750999,50999],"./code.svg":[916981,16981],"./cog.svg":[45962,45962],"./collapse.svg":[424266,24266],"./color_palette.svg":[265580,65580],"./component-style.svg":[903052,3052],"./components.svg":[80312,80312],"./copy.svg":[923141,23141],"./cross-filter-badge.svg":[664625,64625],"./current-rendered-tile.svg":[582955,82955],"./cursor_target.svg":[896758,96758],"./dash-style.svg":[887509,87509],"./dashbord-pcicon.svg":[601893,1893],"./data-sort.svg":[192965,92965],"./database-api.svg":[538692,38692],"./database-menu.svg":[633721,33721],"./database.svg":[815249,15249],"./dataset-excleicon.svg":[212545,12545],"./dataset-sqlicon.svg":[14577,14577],"./dataset-sqllicon.svg":[573903,73903],"./dataset-unionicon.svg":[487157,87157],"./dataset_physical.svg":[308312,8312],"./dataset_virtual.svg":[365330,65330],"./dataset_virtual_greyscale.svg":[84810,84810],"./default_db_image.svg":[551398,51398],"./delete-icon.svg":[452923,52923],"./download-icon.svg":[777227,77227],"./download.svg":[900112,112],"./downone.svg":[565981,65981],"./drag.svg":[886507,86507],"./edit-icon.svg":[737142,37142],"./edit.svg":[793871,93871],"./edit_alt.svg":[986167,86167],"./email.svg":[450504,50504],"./error.svg":[467584,67584],"./error_solid.svg":[525641,25641],"./error_solid_small.svg":[692561,52983],"./error_solid_small_red.svg":[504273,4273],"./exclamation.svg":[235771,35771],"./expand.svg":[147922,47922],"./eye.svg":[911493,11493],"./eye_slash.svg":[239109,39109],"./fangda.svg":[355714,55714],"./favorite-selected.svg":[151568,51568],"./favorite-unselected.svg":[986682,86682],"./favorite_small_selected.svg":[801351,1351],"./field_abc.svg":[470215,70215],"./field_boolean.svg":[687405,87405],"./field_date.svg":[165226,65226],"./field_derived.svg":[644732,44732],"./field_num.svg":[235201,35201],"./field_struct.svg":[391899,91899],"./file-m.svg":[397492,97492],"./file.svg":[620057,20057],"./filter-com.svg":[290944,90944],"./filter-icon.svg":[294266,94266],"./filter.svg":[519305,19305],"./filter_small.svg":[954474,54474],"./folder-m.svg":[71669,71669],"./folder.svg":[686420,86420],"./full-screen.svg":[263058,63058],"./full.svg":[923985,23985],"./function_x.svg":[244662,44662],"./gear.svg":[107610,7610],"./gou.svg":[85429,85429],"./grid.svg":[68425,68425],"./header-icon.svg":[967339,67339],"./image.svg":[692264,92264],"./import.svg":[142698,42698],"./info-solid.svg":[871605,71605],"./info.svg":[2713,2713],"./info_solid_small.svg":[733606,33606],"./join.svg":[985998,85998],"./keyboard.svg":[587850,87850],"./layers.svg":[785832,85832],"./layout-element.svg":[778644,78644],"./left-do.svg":[409403,9403],"./lightbulb.svg":[854797,54797],"./line-chart-tile.svg":[888491,88491],"./link.svg":[899558,99558],"./list.svg":[845707,45707],"./list_view.svg":[938682,38682],"./location.svg":[361174,61174],"./lock_locked.svg":[155359,55359],"./lock_unlocked.svg":[906207,6207],"./map.svg":[18463,18463],"./message.svg":[664458,64458],"./minus.svg":[697183,97183],"./minus_solid.svg":[706371,6371],"./more-setting.svg":[657075,57075],"./more.svg":[424536,24536],"./more_horiz.svg":[339325,39325],"./more_vert.svg":[991185,91185],"./move.svg":[74139,74139],"./name-sort.svg":[755348,55348],"./nav_charts.svg":[275350,75350],"./nav_dashboard.svg":[666303,66303],"./nav_data.svg":[402267,2267],"./nav_explore.svg":[983749,83749],"./nav_home.svg":[844667,44667],"./nav_lab.svg":[743567,43567],"./note.svg":[246597,86126],"./offline.svg":[153265,53265],"./paperclip.svg":[522079,22079],"./pie-chart-tile.svg":[809873,9873],"./placeholder.svg":[318349,18349],"./plus.svg":[817460,17460],"./plus_large.svg":[566150,66150],"./plus_small.svg":[396447,96447],"./plus_solid.svg":[470600,70600],"./queued.svg":[963240,63240],"./recent-sort.svg":[276875,76875],"./redo.svg":[799207,99207],"./refresh.svg":[425367,25367],"./reload.svg":[667049,67049],"./review.svg":[396634,96634],"./right-do.svg":[316389,16389],"./running.svg":[505224,5224],"./save.svg":[136254,36254],"./search.svg":[230177,30177],"./search2.svg":[499064,99064],"./server.svg":[811075,11075],"./share-icon.svg":[806377,6377],"./share.svg":[311263,11263],"./shunxu.svg":[543027,43027],"./slack.svg":[342439,42439],"./sort.svg":[520336,20336],"./sort_asc.svg":[579393,79393],"./sort_desc.svg":[732646,32646],"./sql.svg":[113325,13325],"./table-chart-tile.svg":[804421,4421],"./table.svg":[772403,72403],"./tag.svg":[530158,30158],"./tags.svg":[890363,90363],"./tiaozhuan-setting.svg":[383346,83346],"./transparent.svg":[487803,87803],"./trash.svg":[362105,62105],"./triangle_change.svg":[498398,98398],"./triangle_down.svg":[240826,40826],"./triangle_up.svg":[936819,36819],"./undo.svg":[239622,39622],"./up-level.svg":[165972,65972],"./upone.svg":[873830,73830],"./user.svg":[899767,99767],"./view-detail.svg":[335520,35520],"./view-search.svg":[500916,916],"./view-sort.svg":[731218,31218],"./warning.svg":[404758,4758],"./warning_solid.svg":[275224,75224],"./x-large.svg":[863955,63955],"./x-small.svg":[107716,7716],"./zhidi.svg":[119357,19357],"./zhiding.svg":[244626,44626]};function r(e){if(!n.o(o,e))return Promise.resolve().then((()=>{var t=new Error("Cannot find module '"+e+"'");throw t.code="MODULE_NOT_FOUND",t}));var t=o[e],r=t[0];return n.e(t[1]).then((()=>n(r)))}r.keys=()=>Object.keys(o),r.id=335782,e.exports=r}}]);