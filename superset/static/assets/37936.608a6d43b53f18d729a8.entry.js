"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[37936],{281788:(e,t,o)=>{o.d(t,{B8:()=>d,TZ:()=>s,mf:()=>l,u7:()=>i});var a=o(431069),n=o(68492);const r=(e,t,o)=>{let a=`api/v1/dashboard/${e}/filter_state`;return t&&(a=a.concat(`/${t}`)),o&&(a=a.concat(`?tab_id=${o}`)),a},s=(e,t,o,s)=>a.Z.put({endpoint:r(e,o,s),jsonPayload:{value:t}}).then((e=>e.json.message)).catch((e=>(n.Z.error(e),null))),i=(e,t,o)=>a.Z.post({endpoint:r(e,void 0,o),jsonPayload:{value:t}}).then((e=>e.json.key)).catch((e=>(n.Z.error(e),null))),d=(e,t)=>a.Z.get({endpoint:r(e,t)}).then((({json:e})=>JSON.parse(e.value))).catch((e=>(n.Z.error(e),null))),l=e=>a.Z.get({endpoint:`/api/v1/dashboard/permalink/${e}`}).then((({json:e})=>e)).catch((e=>(n.Z.error(e),null)))},637936:(e,t,o)=>{o.r(t),o.d(t,{DashboardPage:()=>J,DashboardPageIdContext:()=>M,MigrationContext:()=>L,default:()=>V});var a=o(667294),n=o(616550),r=o(751995),s=o(593185),i=o(478161),d=o(328062),l=o(455867),c=o(478718),u=o.n(c),p=o(828216),h=o(211965),f=o(414114),m=o(838703),b=o(774069),_=o(835932);const g=(0,r.iK)(b.Z)`
  .modal-content {
    height: 900px;
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }

  .modal-header {
    flex: 0 1 auto;
  }

  .modal-body {
    flex: 1 1 auto;
    overflow: auto;
  }

  .modal-footer {
    flex: 0 1 auto;
  }

  .ant-modal-body {
    overflow: auto;
  }
`,v=({onClickReview:e,onClickSnooze:t,onHide:o,show:n,hideFooter:r=!1})=>(0,h.tZ)(g,{show:n,onHide:o,title:(0,l.t)("Ready to review filters in this dashboard?"),hideFooter:r,footer:(0,h.tZ)(a.Fragment,null,(0,h.tZ)(_.Z,{buttonSize:"small",onClick:t},(0,l.t)("Remind me in 24 hours")),(0,h.tZ)(_.Z,{buttonSize:"small",onClick:o},(0,l.t)("Cancel")),(0,h.tZ)(_.Z,{buttonSize:"small",buttonStyle:"primary",onClick:e},(0,l.t)("Start Review"))),responsive:!0},(0,h.tZ)("div",null,(0,l.t)("filter_box will be deprecated in a future version of Superset. Please replace filter_box by dashboard filter components.")));var x=o(442582),y=o(182140),S=o(550810),E=o(514505),w=o(107447),Z=o(961337),I=o(269856),O=o(427600),R=o(23525),$=o(653002),j=o(152794),C=o(909467),D=o(281788);const N=e=>h.iv`
  body {
    h1 {
      font-weight: ${e.typography.weights.bold};
      line-height: 1.4;
      font-size: ${e.typography.sizes.xxl}px;
      letter-spacing: -0.2px;
      margin-top: ${3*e.gridUnit}px;
      margin-bottom: ${3*e.gridUnit}px;
    }

    h2 {
      font-weight: ${e.typography.weights.bold};
      line-height: 1.4;
      font-size: ${e.typography.sizes.xl}px;
      margin-top: ${3*e.gridUnit}px;
      margin-bottom: ${2*e.gridUnit}px;
    }

    h3,
    h4,
    h5,
    h6 {
      font-weight: ${e.typography.weights.bold};
      line-height: 1.4;
      font-size: ${e.typography.sizes.l}px;
      letter-spacing: 0.2px;
      margin-top: ${2*e.gridUnit}px;
      margin-bottom: ${e.gridUnit}px;
    }
  }
`,k=e=>h.iv`
  .filter-card-popover {
    width: 240px;
    padding: 0;
    border-radius: 4px;

    &.ant-popover-placement-bottom {
      padding-top: ${e.gridUnit}px;
    }

    &.ant-popover-placement-left {
      padding-right: ${3*e.gridUnit}px;
    }

    .ant-popover-inner {
      box-shadow: 0 0 8px rgb(0 0 0 / 10%);
    }

    .ant-popover-inner-content {
      padding: ${4*e.gridUnit}px;
    }

    .ant-popover-arrow {
      display: none;
    }
  }

  .filter-card-tooltip {
    &.ant-tooltip-placement-bottom {
      padding-top: 0;
      & .ant-tooltip-arrow {
        top: -13px;
      }
    }
  }
`;var T=o(714670),z=o.n(T),F=o(52004),P=o(643399);const L=a.createContext(I.Qi.NOOP),M=a.createContext("");(0,w.Z)();const B=a.lazy((()=>Promise.all([o.e(79521),o.e(19755),o.e(26272),o.e(7734),o.e(54680),o.e(83529),o.e(37672),o.e(5878),o.e(60199),o.e(70463),o.e(83982),o.e(76962),o.e(93197),o.e(88274),o.e(86992),o.e(93630),o.e(73942),o.e(80801),o.e(60452)]).then(o.bind(o,60071)))),Q=document.title,U=()=>{const e=(0,Z.rV)(Z.dR.dashboard__explore_context,{});return Object.fromEntries(Object.entries(e).filter((([,e])=>!e.isRedundant)))},A=(e,t)=>{const o=U();(0,Z.LS)(Z.dR.dashboard__explore_context,{...o,[e]:t})},J=({idOrSlug:e,dashboardShare:t,handleRemoveId:o,searchParams:c})=>{const b=(0,p.I0)(),_=(0,r.Fg)(),g=(0,n.k6)(),w=(0,p.v9)((e=>e.user)),T=(0,p.v9)((e=>e.dashboardState.editMode)),J=(0,p.v9)((e=>e.dashboardState.layoutMode||F.kB.PC)),V=(()=>{const e=(0,a.useMemo)((()=>z().generate()),[]),t=(0,p.v9)((({dashboardInfo:t,dashboardState:o,nativeFilters:a,dataMask:n})=>{var r,s,i;return{labelColors:(null==(r=t.metadata)?void 0:r.label_colors)||{},sharedLabelColors:(null==(s=t.metadata)?void 0:s.shared_label_colors)||{},colorScheme:null==o?void 0:o.colorScheme,chartConfiguration:(null==(i=t.metadata)?void 0:i.chart_configuration)||{},nativeFilters:Object.entries(a.filters).reduce(((e,[t,o])=>({...e,[t]:u()(o,["chartsInScope"])})),{}),dataMask:n,dashboardId:t.id,filterBoxFilters:(0,P.De)(),dashboardPageId:e}}));return(0,a.useEffect)((()=>(A(e,t),()=>{A(e,{...t,isRedundant:!0})})),[t,e]),e})(),{addDangerToast:H}=(0,f.e1)(),{result:K,status:Y}=(0,x.QU)(e),{result:q}=(0,x.Es)(e),{result:W,error:G,status:X}=(0,x.JL)(e),ee=(0,a.useRef)(!1),te=(0,R.VW)();let oe="";"error"!=Y||K||(sessionStorage.removeItem("daidOrSlug_ids"),sessionStorage.removeItem("isperm"),o&&o(-1)),c&&Object.prototype.hasOwnProperty.call(c,"target_id")&&q&&W&&(null==q||q.forEach((e=>{const t=e.form_data.datasource.split("__")[0],o=W.filter((e=>e.id==t));if(o.length>0)for(const t in c){const a=o[0].columns.some((e=>e.column_name===t)),n=e.form_data.adhoc_filters.findIndex((e=>e.subject===t));n>-1?e.form_data.adhoc_filters[n].comparator=c[t]:a&&e.form_data.adhoc_filters.push({clause:"WHERE",comparator:c[t],expressionType:"SIMPLE",operator:"IN",subject:t})}}))),te.control&&te.control.data.actions.forEach((e=>{oe=e.thirdTag})),K&&oe&&(K.third_tags=oe);const ae=Boolean(K&&q),ne=(0,R.eY)(O.KD.migrationState),re=(0,s.c)(s.T.ENABLE_FILTER_BOX_MIGRATION),{dashboard_title:se,css:ie,metadata:de,id:le=0}=K||{},[ce,ue]=(0,a.useState)(ne||I.Qi.NOOP);return(0,a.useEffect)((()=>{const e=()=>{const e=U();(0,Z.LS)(Z.dR.dashboard__explore_context,{...e,[V]:{...e[V],isRedundant:!0}})};return window.addEventListener("beforeunload",e),()=>{window.removeEventListener("beforeunload",e)}}),[V]),(0,a.useEffect)((()=>{b((0,C.sL)(X))}),[b,X]),(0,a.useEffect)((()=>{b((0,C.$D)(t||!1))}),[b,t]),(0,a.useEffect)((()=>{const e=null==q?void 0:q.some((e=>{var t;return"filter_box"===(null==(t=e.form_data)?void 0:t.viz_type)}));if(K&&(0,$.Ms)(K,w)){if(null!=de&&de.native_filter_configuration)return void ue(re?I.Qi.CONVERTED:I.Qi.NOOP);if(e)if(re){if(ne&&Object.values(I.Qi).includes(ne))return void ue(ne);const e=(0,Z.rV)(Z.dR.filter_box_transition_snoozed_at,{});if(Date.now()-(e[le]||0)<I.Yd)return void ue(I.Qi.SNOOZED);ue(I.Qi.UNDECIDED)}else(0,s.c)(s.T.DASHBOARD_NATIVE_FILTERS)}}),[ae]),(0,a.useEffect)((()=>{le&&async function(){const e=(0,R.eY)(O.KD.permalinkKey),t=(0,R.eY)(O.KD.nativeFiltersKey),o=(0,R.eY)(O.KD.nativeFilters);let a,n=t||{};if(e){const t=await(0,D.mf)(e);t&&({dataMask:n,activeTabs:a}=t.state)}else t&&(n=await(0,D.B8)(le,t));o&&(n=o),ae&&(ee.current||(ee.current=!0,(0,s.c)(s.T.DASHBOARD_NATIVE_FILTERS_SET)&&b((0,j.pi)(le))),b((0,y.Y)({history:g,dashboard:K,charts:q,activeTabs:a,filterboxMigrationState:ce,dataMask:n})))}()}),[ae,ce]),(0,a.useEffect)((()=>(se&&(document.title=se),()=>{document.title=Q})),[se]),(0,a.useEffect)((()=>"string"===typeof ie?(0,E.Z)(ie):()=>{}),[ie]),(0,a.useEffect)((()=>{const e=(0,i.ZP)();return e.source=i.Ag.dashboard,()=>{d.getNamespace(null==de?void 0:de.color_namespace).resetColors(),e.clear()}}),[null==de?void 0:de.color_namespace]),(0,a.useEffect)((()=>{G?H((0,l.t)("Error loading chart datasources. Filters may not work correctly.")):b((0,S.Fy)(W))}),[H,W,G,b]),(0,a.useEffect)((()=>{T||J!==F.kB.MOBILE||(document.body.style.overflow="hidden")}),[]),ae||"loading"!=Y?(0,h.tZ)(a.Fragment,null,(0,h.tZ)(h.xB,{styles:[k(_),N(_),"",""]}),(0,h.tZ)(v,{show:ce===I.Qi.UNDECIDED,hideFooter:!re,onHide:()=>{ue(I.Qi.SNOOZED)},onClickReview:()=>{ue(I.Qi.REVIEWING)},onClickSnooze:()=>{const e=(0,Z.rV)(Z.dR.filter_box_transition_snoozed_at,{});(0,Z.LS)(Z.dR.filter_box_transition_snoozed_at,{...e,[le]:Date.now()}),ue(I.Qi.SNOOZED)}}),(0,h.tZ)(L.Provider,{value:ce},(0,h.tZ)(M.Provider,{value:V},(0,h.tZ)(B,null)))):(0,h.tZ)(m.Z,null)},V=J},514505:(e,t,o)=>{function a(e){const t="CssEditor-css",o=document.head||document.getElementsByTagName("head")[0],a=document.querySelector(`.${t}`)||function(e){const t=document.createElement("style");return t.className=e,t.type="text/css",t}(t);return"styleSheet"in a?a.styleSheet.cssText=e:a.innerHTML=e,o.appendChild(a),function(){a.remove()}}o.d(t,{Z:()=>a})},442582:(e,t,o)=>{o.d(t,{s_:()=>a.s_,hb:()=>d,QU:()=>l,Es:()=>c,JL:()=>u,Xx:()=>m,zA:()=>b});var a=o(242190),n=o(115926),r=o.n(n);function s({owners:e}){return e?e.map((e=>`${e.first_name} ${e.last_name}`)):null}const i=r().encode({columns:["owners.first_name","owners.last_name"],keys:["none"]});function d(e){return(0,a.l6)((0,a.s_)(`/api/v1/chart/${e}?q=${i}`),s)}const l=e=>(0,a.l6)((0,a.s_)(`/api/v1/dashboard/${e}`),(e=>({...e,metadata:e.json_metadata&&JSON.parse(e.json_metadata)||{},position_data:e.position_json&&JSON.parse(e.position_json),mobile_metadata:e.mobile_json_metadata&&JSON.parse(e.mobile_json_metadata)||{},mobile_position_data:e.mobile_position_json&&JSON.parse(e.mobile_position_json)||e.mobile_json_metadata&&JSON.parse(e.mobile_json_metadata).positions||{}}))),c=e=>(0,a.s_)(`/api/v1/dashboard/${e}/charts`),u=e=>(0,a.s_)(`/api/v1/dashboard/${e}/datasets`);var p=o(667294),h=o(388767),f=o(431069);function m(e){const{dbId:t,onSuccess:o,onError:a}=e||{},n=(0,p.useRef)(!1),s={dbId:t},i=(0,h.useQuery)(["schemas",{dbId:t}],(()=>function({dbId:e,forceRefresh:t}){const o=`/api/v1/database/${e}/schemas/?q=${r().encode({force:t})}`;return f.Z.get({endpoint:o})}({...s,forceRefresh:n.current})),{select:({json:e})=>e.result.map((e=>({value:e,label:e,title:e}))),enabled:Boolean(t),onSuccess:o,onError:a,onSettled:()=>{n.current=!1}});return{...i,refetch:()=>(n.current=!0,i.refetch())}}function b(e){const{data:t,isFetching:o}=m({dbId:e.dbId}),a=(0,p.useMemo)((()=>new Set(null==t?void 0:t.map((({value:e})=>e)))),[t]),{dbId:n,schema:s,onSuccess:i,onError:d}=e||{},l=(0,p.useRef)(!1),c={dbId:n,schema:s},u=(0,h.useQuery)(["tables",{dbId:n,schema:s}],(()=>function({dbId:e,schema:t,forceRefresh:o}){const a=t?encodeURIComponent(t):"",n=`/api/v2/database/${null!=e?e:"undefined"}/tables/?q=${r().encode({force:o,schema_name:a})}`;return f.Z.get({endpoint:n})}({...c,forceRefresh:l.current})),{select:({json:e})=>({options:e.result,hasMore:e.count>e.result.length}),enabled:Boolean(n&&s&&!o&&a.has(s)),onSuccess:i,onError:d,onSettled:()=>{l.current=!1}});return{...u,refetch:()=>(l.current=!0,u.refetch())}}}}]);