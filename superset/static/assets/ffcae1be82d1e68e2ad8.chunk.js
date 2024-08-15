"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[37633],{882842:(e,t,a)=>{a.r(t),a.d(t,{default:()=>P});var s=a(667294),l=a(751995),r=a(455867),n=a(431069),o=a(343716),i=a(730381),c=a.n(i),d=a(667496),u=a(440768),p=a(414114),m=a(34858),g=a(620755),h=a(976697),b=a(495413),y=a(418782),Z=a(358593),v=a(242110),q=a(833743),x=a(600120),f=a(427600),w=a(400012),C=a(731293),S=a(774069),$=a(294184),k=a.n($),T=a(835932),_=a(331673),z=a(14025),D=a(211965);const H=l.iK.div`
  color: ${({theme:e})=>e.colors.secondary.light2};
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
  margin-bottom: 0;
  text-transform: uppercase;
`,U=l.iK.div`
  color: ${({theme:e})=>e.colors.grayscale.dark2};
  font-size: ${({theme:e})=>e.typography.sizes.m}px;
  padding: 4px 0 24px 0;
`,L=l.iK.div`
  margin: 0 0 ${({theme:e})=>6*e.gridUnit}px 0;
`,J=l.iK.div`
  display: inline;
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
  padding: ${({theme:e})=>2*e.gridUnit}px
    ${({theme:e})=>4*e.gridUnit}px;
  margin-right: ${({theme:e})=>4*e.gridUnit}px;
  color: ${({theme:e})=>e.colors.secondary.dark1};

  &.active,
  &:focus,
  &:hover {
    background: ${({theme:e})=>e.colors.secondary.light4};
    border-bottom: none;
    border-radius: ${({theme:e})=>e.borderRadius}px;
    margin-bottom: ${({theme:e})=>2*e.gridUnit}px;
  }

  &:hover:not(.active) {
    background: ${({theme:e})=>e.colors.secondary.light5};
  }
`,I=(0,l.iK)(S.Z)`
  .ant-modal-body {
    padding: ${({theme:e})=>6*e.gridUnit}px;
  }

  pre {
    font-size: ${({theme:e})=>e.typography.sizes.xs}px;
    font-weight: ${({theme:e})=>e.typography.weights.normal};
    line-height: ${({theme:e})=>e.typography.sizes.l}px;
    height: 375px;
    border: none;
  }
`;const N=(0,p.ZP)((function({onHide:e,openInSqlLab:t,queries:a,query:l,fetchData:n,show:o,addDangerToast:i,addSuccessToast:c}){const{handleKeyPress:d,handleDataChange:u,disablePrevious:p,disableNext:m}=(0,z.Cq)({queries:a,currentQueryId:l.id,fetchData:n}),[g,h]=(0,s.useState)("user"),{id:b,sql:y,executed_sql:Z}=l;return(0,D.tZ)("div",{role:"none",onKeyUp:d},(0,D.tZ)(I,{onHide:e,show:o,title:(0,r.t)("Query preview"),footer:(0,D.tZ)(s.Fragment,null,(0,D.tZ)(T.Z,{"data-test":"previous-query",key:"previous-query",disabled:p,onClick:()=>u(!0)},(0,r.t)("Previous")),(0,D.tZ)(T.Z,{"data-test":"next-query",key:"next-query",disabled:m,onClick:()=>u(!1)},(0,r.t)("Next")),(0,D.tZ)(T.Z,{"data-test":"open-in-sql-lab",key:"open-in-sql-lab",buttonStyle:"primary",onClick:()=>t(b)},(0,r.t)("Open in SQL Lab")))},(0,D.tZ)(H,null,(0,r.t)("Tab name")),(0,D.tZ)(U,null,l.tab_name),(0,D.tZ)(L,null,(0,D.tZ)(J,{role:"button","data-test":"toggle-user-sql",className:k()({active:"user"===g}),onClick:()=>h("user")},(0,r.t)("User query")),(0,D.tZ)(J,{role:"button","data-test":"toggle-executed-sql",className:k()({active:"executed"===g}),onClick:()=>h("executed")},(0,r.t)("Executed query"))),(0,D.tZ)(_.Z,{addDangerToast:i,addSuccessToast:c,language:"sql"},("user"===g?y:Z)||"")))})),K=(0,l.iK)(y.Z)`
  table .table-cell {
    vertical-align: top;
  }
`;v.Z.registerLanguage("sql",q.Z);const E=(0,l.iK)(v.Z)`
  height: ${({theme:e})=>26*e.gridUnit}px;
  overflow: hidden !important; /* needed to override inline styles */
  text-overflow: ellipsis;
  white-space: nowrap;
`,O=l.iK.div`
  .count {
    margin-left: 5px;
    color: ${({theme:e})=>e.colors.primary.base};
    text-decoration: underline;
    cursor: pointer;
  }
`,j=l.iK.div`
  color: ${({theme:e})=>e.colors.grayscale.dark2};
`;const P=(0,p.ZP)((function({addDangerToast:e}){const{state:{loading:t,resourceCount:a,resourceCollection:i},fetchData:p}=(0,m.Yi)("query",(0,r.t)("Query history"),e,!1),[v,q]=(0,s.useState)(),S=(0,l.Fg)(),$=(0,s.useCallback)((t=>{n.Z.get({endpoint:`/api/v1/query/${t}`}).then((({json:e={}})=>{q({...e.result})}),(0,u.v$)((t=>e((0,r.t)("There was an issue previewing the selected query. %s",t)))))}),[e]),k=[];b.Y.tabs.map((e=>{e.show&&k.push(e)}));const T={activeChild:"Query history",...b.Y,tabs:k},_=[{id:w.J.start_time,desc:!0}],z=(0,s.useMemo)((()=>[{Cell:({row:{original:{status:e}}})=>{const t={name:null,label:""};return e===o.Tb.SUCCESS?(t.name=(0,D.tZ)(C.Z.Check,{iconColor:S.colors.success.base}),t.label=(0,r.t)("Success")):e===o.Tb.FAILED||e===o.Tb.STOPPED?(t.name=(0,D.tZ)(C.Z.XSmall,{iconColor:e===o.Tb.FAILED?S.colors.error.base:S.colors.grayscale.base}),t.label=(0,r.t)("Failed")):e===o.Tb.RUNNING?(t.name=(0,D.tZ)(C.Z.Running,{iconColor:S.colors.primary.base}),t.label=(0,r.t)("Running")):e===o.Tb.TIMED_OUT?(t.name=(0,D.tZ)(C.Z.Offline,{iconColor:S.colors.grayscale.light1}),t.label=(0,r.t)("Offline")):e!==o.Tb.SCHEDULED&&e!==o.Tb.PENDING||(t.name=(0,D.tZ)(C.Z.Queued,{iconColor:S.colors.grayscale.base}),t.label=(0,r.t)("Scheduled")),(0,D.tZ)(Z.u,{title:t.label,placement:"bottom"},(0,D.tZ)("span",null,t.name))},accessor:w.J.status,size:"xs",disableSortBy:!0},{accessor:w.J.start_time,Header:(0,r.t)("Time"),size:"xl",Cell:({row:{original:{start_time:e,end_time:t}}})=>{const a=c().utc(e).local().format(f.v2).split(" "),l=(0,D.tZ)(s.Fragment,null,a[0]," ",(0,D.tZ)("br",null),a[1]);return t?(0,D.tZ)(Z.u,{title:(0,r.t)("Duration: %s",c()(c().utc(t-e)).format(f.n2)),placement:"bottom"},(0,D.tZ)("span",null,l)):l}},{accessor:w.J.tab_name,Header:(0,r.t)("Tab name"),size:"xl"},{accessor:w.J.database_name,Header:(0,r.t)("Database"),size:"xl"},{accessor:w.J.database,hidden:!0},{accessor:w.J.schema,Header:(0,r.t)("Schema"),size:"xl"},{Cell:({row:{original:{sql_tables:e=[]}}})=>{const t=e.map((e=>e.table)),a=t.length>0?t.shift():"";return t.length?(0,D.tZ)(O,null,(0,D.tZ)("span",null,a),(0,D.tZ)(h.ZP,{placement:"right",title:(0,r.t)("TABLES"),trigger:"click",content:(0,D.tZ)(s.Fragment,null,t.map((e=>(0,D.tZ)(j,{key:e},e))))},(0,D.tZ)("span",{className:"count"},"(+",t.length,")"))):a},accessor:w.J.sql_tables,Header:(0,r.t)("Tables"),size:"xl",disableSortBy:!0},{accessor:w.J.user_first_name,Header:(0,r.t)("User"),size:"xl",Cell:({row:{original:{user:e}}})=>e?`${e.first_name} ${e.last_name}`:""},{accessor:w.J.user,hidden:!0},{accessor:w.J.rows,Header:(0,r.t)("Rows"),size:"md"},{accessor:w.J.sql,Header:(0,r.t)("SQL"),Cell:({row:{original:e,id:t}})=>(0,D.tZ)("div",{tabIndex:0,role:"button","data-test":`open-sql-preview-${t}`,onClick:()=>q(e)},(0,D.tZ)(E,{language:"sql",style:x.Z},(0,u.IB)(e.sql,4)))},{Header:(0,r.t)("Actions"),id:"actions",disableSortBy:!0,Cell:({row:{original:{id:e}}})=>(0,D.tZ)(Z.u,{title:(0,r.t)("Open query in SQL Lab"),placement:"bottom"},(0,D.tZ)("a",{href:(0,d.VU)(`/superset/sqllab?queryId=${e}`)},(0,D.tZ)(C.Z.Full,{iconColor:S.colors.grayscale.base})))}]),[]),H=(0,s.useMemo)((()=>async()=>n.Z.get({endpoint:"/api/v2/datasource/database/list/"}).then((e=>{var t,a,s;return e.json.meta.data=(null==e||null==(t=e.json)||null==(a=t.meta)||null==(s=a.data)?void 0:s.map((e=>({value:e.id,label:e.database_name}))))||[],e.json.meta}))),[]),U=(0,s.useCallback)(((e="",t,a)=>{const s=`api/v2/user/?username=${e}&page_index=${t+1}&page_size=${a}`;return n.Z.get({endpoint:s}).then((e=>{var t,a,s,l,r,n;const o=JSON.parse(JSON.stringify(e));return o.json.meta.data=(null==e||null==(t=e.json)||null==(a=t.meta)||null==(s=a.data)?void 0:s.list.map((e=>({value:e.id,label:e.cn_name}))))||[],o.json.meta.totalCount=null==e||null==(l=e.json)||null==(r=l.meta)||null==(n=r.data)?void 0:n.count,o.json.meta}))}),[]),L=(0,s.useMemo)((()=>[{Header:(0,r.t)("Database"),key:"database",id:"database",input:"select",operator:y.p.relationOneMany,unfilteredLabel:(0,r.t)("All"),fetchSelects:H,paginate:!0},{Header:(0,r.t)("State"),key:"state",id:"status",input:"select",operator:y.p.equals,unfilteredLabel:"All",fetchSelects:(0,u.wk)("query","status",(0,u.v$)((t=>e((0,r.t)("An error occurred while fetching schema values: %s",t))))),paginate:!0},{Header:(0,r.t)("User"),key:"user",id:"user",input:"select",operator:y.p.relationOneMany,unfilteredLabel:"All",fetchSelects:U,paginate:!0},{Header:(0,r.t)("Time range"),key:"start_time",id:"start_time",input:"datetime_range",operator:y.p.between},{Header:(0,r.t)("Search by query text"),key:"sql",id:"sql",input:"search",operator:y.p.contains}]),[e]);return(0,D.tZ)("div",{style:{paddingTop:50}},(0,D.tZ)(g.Z,T),v&&(0,D.tZ)(N,{onHide:()=>q(void 0),query:v,queries:i,fetchData:$,openInSqlLab:e=>window.location.assign((0,d.VU)(`/superset/sqllab?queryId=${e}`)),show:!0}),(0,D.tZ)("div",{style:{overflowY:"auto",maxHeight:"calc(100vh - 126px)"}},(0,D.tZ)(K,{className:"query-history-list-view",columns:z,count:a,data:i,fetchData:p,filters:L,initialSort:_,loading:t,pageSize:25,highlightRowId:null==v?void 0:v.id})))}))}}]);