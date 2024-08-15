"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[39458],{112515:(e,t,n)=>{n.d(t,{AH:()=>D,CB:()=>w,H6:()=>v,Jp:()=>h,bX:()=>x,kN:()=>y,kP:()=>I,mG:()=>Z,pd:()=>O,pe:()=>L,u:()=>R,xW:()=>T,y8:()=>N});var r=n(667294),a=n(354998),o=n.n(a),i=n(311064),s=n(719427),l=n(861654),c=n(431069),d=n(355786),u=n(986374),_=n(309679),m=n(454076),p=n(427600),E=n(269856),g=n(680621);function h(e){var t,n;const{slice:r,form_data:a}=e;return null!=(t=null!=(n=null==r?void 0:r.slice_id)?n:null==a?void 0:a.slice_id)?t:E.xA}let f=0;function A(e=!1){let t=0;return e&&(t=f%u.X.length,f+=1,0===t&&(t+=1,f+=1)),u.X[t]}function T(e,t){if(null===e||void 0===e)return null;return o()(window.location.search).pathname("/api/v1/chart/data").search({form_data:(0,_.o)({slice_id:e}),force:t}).toString()}const S="";function b(e="base"){return["full","json","csv","query","results","samples"].includes(e)?`${S}/superset/explore_json/`:"/explore/"}function N(e,t={},n=!1){const r=new(o())("/"),a=b(e),i=r.search(!0);return Object.keys(t).forEach((e=>{i[e]=t[e]})),e===p.KD.standalone.name&&(n&&(i.force="1"),i.standalone=g._B.HIDE_NAV),r.directory(a).search(i).toString()}function y({path:e,qs:t,allowDomainSharding:n=!1}){let r=new(o())({protocol:window.location.protocol.slice(0,-1),hostname:A(n),port:window.location.port?window.location.port:"",path:e});return t&&(r=r.search(t)),r}function v({formData:e,endpointType:t="base",force:n=!1,curUrl:r=null,requestParams:a={},allowDomainSharding:i=!1,method:s="POST"}){if(!e.datasource)return null;delete e.label_colors;let l=y({path:"/",allowDomainSharding:i});r&&(l=o()(o()(r).search()));const c=b(t),d=l.search(!0),{slice_id:u,extra_filters:m,adhoc_filters:E,viz_type:g}=e;if(u){const e={slice_id:u};"GET"===s&&(e.viz_type=g,m&&m.length&&(e.extra_filters=m),E&&E.length&&(e.adhoc_filters=E)),d.form_data=(0,_.o)(e)}n&&(d.force="true"),"csv"===t&&(d.csv="true"),t===p.KD.standalone.name&&(d.standalone="1"),"query"===t&&(d.query="true"),"results"===t&&(d.results="true"),"samples"===t&&(d.samples="true");const h=Object.keys(a);return h.length&&h.forEach((e=>{a.hasOwnProperty(e)&&(d[e]=a[e])})),l.search(d).directory(c).toString()}const I=e=>{const t=(0,i.Z)().get(e.viz_type);return!!t&&t.useLegacyApi},R=({formData:e,force:t,resultFormat:n,resultType:r,setDataMask:a,ownState:o})=>{var i;return(null!=(i=(0,s.Z)().get(e.viz_type))?i:e=>(0,l.Z)(e,(e=>[{...e}])))({...e,force:t,result_format:n,result_type:r},{ownState:o,hooks:{setDataMask:a}})},O=({resultType:e,resultFormat:t})=>"csv"===t?t:e,L=({formData:e,resultFormat:t="json",resultType:n="full",force:r=!1,ownState:a={}})=>{let o,i;if(I(e)){o=v({formData:e,endpointType:O({resultFormat:t,resultType:n}),allowDomainSharding:!1}),i=e}else o="/api/v1/chart/data",i=R({formData:e,force:r,resultFormat:t,resultType:n,ownState:a});c.Z.postForm(o,{form_data:(0,_.o)(i)})},D=(e,t)=>{const n=v({formData:e,endpointType:"base",allowDomainSharding:!1,requestParams:t});c.Z.postForm(n,{form_data:(0,_.o)(e)})},x=(e,t,n)=>{const a=(0,r.useCallback)(e,n);(0,r.useEffect)((()=>{const e=setTimeout((()=>{a()}),t);return()=>{clearTimeout(e)}}),[a,t])},w=(e,t,n)=>{const r=[...E.qK].map((e=>E.LT[e].operation)).indexOf(t)>=0;let a=null!=e?e:"";if(e&&t){a+=` ${t}`;const e=r&&Array.isArray(n)?n[0]:n,o=(0,d.Z)(n),i=void 0!==e&&Number.isNaN(Number(e)),s=i?"'":"",[l,c]=r?["(",")"]:["",""],u=o.map((e=>(0,m.lo)(e))).map((e=>`${s}${i?String(e).replace("'","''"):e}${s}`));o.length>0&&(a+=` ${l}${u.join(", ")}${c}`)}return a};function Z(e){return e.map((e=>[e,e.toString()]))}},479217:(e,t,n)=>{n.d(t,{z:()=>r});const r=e=>{var t;return{columns:e.columns,name:(null==e?void 0:e.datasource_name)||(null==e?void 0:e.name)||"Untitled",dbId:(null==e||null==(t=e.database)?void 0:t.id)||(null==e?void 0:e.dbId),sql:(null==e?void 0:e.sql)||"",schema:null==e?void 0:e.schema}}},444814:(e,t,n)=>{n.d(t,{zO:()=>i,zQ:()=>o});var r=n(730381),a=n.n(r);const o=function(e,t,n="HH:mm:ss.SS"){const r=t-e;return a()(new Date(r)).utc().format(n)},i=function(){return a()().utc().valueOf()}},986374:(e,t,n)=>{n.d(t,{X:()=>i,_:()=>s});var r=n(591877),a=n(593185),o=n(920292);const i=function(){if(!document.getElementById("app"))return[];const e=new Set([window.location.hostname]);if("1"===new URLSearchParams(window.location.search).get("disableDomainSharding"))return Array.from(e);const t=(0,o.Z)();return(0,r.fG)(t.common.feature_flags),(0,r.cr)(a.T.ALLOW_DASHBOARD_DOMAIN_SHARDING)&&t&&t.common&&t.common.conf&&t.common.conf.SUPERSET_WEBSERVER_DOMAINS&&t.common.conf.SUPERSET_WEBSERVER_DOMAINS.forEach((t=>{e.add(t)})),Array.from(e)}(),s=i.length>1},409882:(e,t,n)=>{n.d(t,{V:()=>l,Z:()=>c});var r=n(121804),a=n.n(r),o=(n(667294),n(455867)),i=n(51776),s=n(211965);function l({label:e,tooltip:t,bsStyle:n,onClick:r,icon:l="info-circle",className:c="text-muted",placement:d="right",iconsStyle:u={}}){const _=`fa fa-${l} ${c} ${n?`text-${n}`:""}`,m=(0,s.tZ)("i",{role:"button","aria-label":(0,o.t)("Show info tooltip"),tabIndex:0,className:_,style:{cursor:r?"pointer":void 0,...u},onClick:r,onKeyPress:r&&(e=>{"Enter"!==e.key&&" "!==e.key||r()})});return t?(0,s.tZ)(i.u,{id:`${a()(e)}-tooltip`,title:t,placement:d},m):m}const c=l},51776:(e,t,n)=>{n.d(t,{Z:()=>d,u:()=>c});var r=n(205872),a=n.n(r),o=n(667294),i=n(751995),s=n(211965),l=n(931097);const c=({overlayStyle:e,color:t,...n})=>{const r=(0,i.Fg)(),c=`${r.colors.grayscale.dark2}e6`;return(0,s.tZ)(o.Fragment,null,(0,s.tZ)(s.xB,{styles:s.iv`
          .ant-tooltip-open {
            display: inline-block;
            &::after {
              content: '';
              display: block;
            }
          }
        `}),(0,s.tZ)(l.Z,a()({overlayStyle:{fontSize:r.typography.sizes.s,lineHeight:"1.6",maxWidth:62*r.gridUnit,minWidth:30*r.gridUnit,...e},align:{offset:[0,1]},color:c||t,trigger:"hover",placement:"bottom",mouseLeaveDelay:0},n)))},d=c},719427:(e,t,n)=>{n.d(t,{Z:()=>i});var r=n(590537),a=n(601875);class o extends r.Z{constructor(){super({name:"ChartBuildQuery",overwritePolicy:r.r.WARN})}}const i=(0,a.Z)(o)},311064:(e,t,n)=>{n.d(t,{Z:()=>i});var r=n(590537),a=n(601875);class o extends r.Z{constructor(){super({name:"ChartMetadata",overwritePolicy:r.r.WARN})}}const i=(0,a.Z)(o)},178186:(e,t,n)=>{n.d(t,{Z:()=>_});var r=n(682492),a=n.n(r),o=n(667294),i=n(349541),s=n(753120),l=n(795518),c=n(189059),d=n(593185),u=n(211965);const _=function({source:e,htmlSanitization:t=!0,htmlSchemaOverrides:n={}}){const r=(0,d.c)(d.T.DISPLAY_MARKDOWN_HTML),_=(0,d.c)(d.T.ESCAPE_MARKDOWN_HTML),m=(0,o.useMemo)((()=>{const e=[];if(r&&!_&&(e.push(c.Z),t)){const t=a()(s.R,n);e.push([l.Z,t])}return e}),[r,_,t,n]);return(0,u.tZ)(i.D,{rehypePlugins:m,skipHtml:!r},e)}},667706:(e,t,n)=>{n.d(t,{Z:()=>a});var r=n(46078);class a{constructor(e){this.id=void 0,this.type=void 0;const[t,n]=e.split("__");this.id=parseInt(t,10),this.type=r.i9.Table,this.type="query"===n?r.i9.Query:this.type}toString(){return`${this.id}__${this.type}`}toObject(){return{id:this.id,type:this.type}}}},861654:(e,t,n)=>{n.d(t,{Z:()=>l});var r=n(365946),a=n(667706),o=n(678444),i=n(111146);const s=e=>[e];function l(e,t){const{queryFields:n,buildQuery:l=s}="function"===typeof t?{buildQuery:t,queryFields:{}}:t||{};let c=l((0,r.Z)(e,n));return c.forEach((e=>{Array.isArray(e.post_processing)&&(e.post_processing=e.post_processing.filter(Boolean))})),(0,i.SR)(e)&&(c=c.map((t=>(0,o.T)(e,t)))),{datasource:new a.Z(e.datasource).toObject(),force:e.force||!1,queries:c,form_data:e,result_format:e.result_format||"json",result_type:e.result_type||"full"}}},365946:(e,t,n)=>{n.d(t,{Z:()=>d});var r=n(62446),a=n(46306),o=n(478483);function i(e){let t=e;return e.includes("--")&&(t=`${e}\n`),`(${t})`}var s=n(569363),l=n(5364);var c=n(237731);function d(e,t){var n,d;const{annotation_layers:u=[],extra_form_data:_,time_range:m,since:p,until:E,row_limit:g,row_offset:h,order_desc:f,limit:A,timeseries_limit_metric:T,granularity:S,url_params:b={},custom_params:N={},series_columns:y,series_limit:v,series_limit_metric:I,...R}=e,{adhoc_filters:O=[],filters:L=[],custom_form_data:D={},...x}=_||{},w=Number(g),Z=Number(h),{metrics:C,columns:U,orderby:$}=(0,s.Z)(R,t),P=function(e){const t={},n=[],r={},a={filters:n,extras:r,applied_time_extras:t},o={__time_range:"time_range",__time_col:"granularity_sqla",__time_grain:"time_grain_sqla",__granularity:"granularity"};return(e.extra_filters||[]).forEach((e=>{if(e.col in o){const n=e.col;a[o[n]]=e.val,t[n]=e.val}else n.push(e)})),r.time_grain_sqla=a.time_grain_sqla||e.time_grain_sqla,a.granularity=a.granularity_sqla||e.granularity||e.granularity_sqla,delete a.granularity_sqla,delete a.time_grain_sqla,a}(e),{filters:B}=P,M={filters:[...B,...L],adhoc_filters:[...e.adhoc_filters||[],...O]},H=function(e){const{adhoc_filters:t,extras:n={},filters:r=[],where:s}=e,l=r,c=[];s&&c.push(s);const d=[];return(t||[]).forEach((e=>{const{clause:t}=e;if((0,a.Ki)(e)){const n=(0,o.Z)(e);"WHERE"===t&&l.push(n)}else{const{sqlExpression:n}=e;"WHERE"===t?c.push(n):d.push(n)}})),n.having=d.map(i).join(" AND "),n.where=c.map(i).join(" AND "),{filters:l,extras:n}}({...e,...P,...M});let k={time_range:m||void 0,since:p||void 0,until:E||void 0,granularity:S||void 0,...P,...H,columns:U,metrics:C,orderby:$,annotation_layers:u,row_limit:null==g||Number.isNaN(w)?void 0:w,row_offset:null==h||Number.isNaN(Z)?void 0:Z,series_columns:y,series_limit:null!=v?v:(0,c.Z)(A)?Number(A):0,series_limit_metric:null!=(n=null!=(d=(e=>{if((0,r.I0)(e))return e})(I))?d:T)?n:void 0,order_desc:"undefined"===typeof f||f,url_params:b||void 0,custom_params:N};return k=function(e,t){const n={...e},{extras:r={}}=n;return Object.entries(l.gn).forEach((([e,r])=>{const a=t[e];void 0!==a&&(n[r]=a)})),l.fn.forEach((e=>{e in t&&(r[e]=t[e])})),Object.keys(r).length>0&&(n.extras=r),n}(k,x),{...k,custom_form_data:D}}},5364:(e,t,n)=>{n.d(t,{Ay:()=>c,Ci:()=>i,NU:()=>l,W3:()=>r,fn:()=>o,gn:()=>s,vM:()=>a});const r="__timestamp",a="No filter",o=["relative_start","relative_end","time_grain_sqla"],i=["adhoc_filters","filters","interactive_groupby","interactive_highlight","interactive_drilldown","custom_form_data"],s={granularity:"granularity",granularity_sqla:"granularity",time_column:"time_column",time_grain:"time_grain",time_range:"time_range"},l=Object.keys(s),c=[...l,...o]},478483:(e,t,n)=>{n.d(t,{Z:()=>a});var r=n(46306);function a(e){const{subject:t}=e;if((0,r._l)(e)){const{operator:n}=e;return{col:t,op:n}}if((0,r.kC)(e)){const{operator:n}=e;return{col:t,op:n,val:e.comparator}}const{operator:n}=e;return{col:t,op:n,val:e.comparator}}},569363:(e,t,n)=>{n.d(t,{Z:()=>c});var r=n(455867),a=n(274765),o=n(5364),i=n(310581),s=n(956652),l=n(920620);function c(e,t){const n={metric:"metrics",metric_2:"metrics",secondary_metric:"metrics",x:"metrics",y:"metrics",size:"metrics",all_columns:"columns",series:"groupby",order_by_cols:"orderby",...t},{query_mode:c,include_time:d,...u}=e;let _=[],m=[],p=[];return Object.entries(u).forEach((([e,t])=>{if(null==t)return;let r=n[e]||e;c===l.n.aggregate&&"columns"===r||(c!==l.n.raw||"groupby"!==r&&"metrics"!==r)&&("groupby"===r&&(r="columns"),"metrics"===r?m=m.concat(t):"columns"===r?_=_.concat(t):"orderby"===r&&(p=p.concat(t)))})),d&&!_.includes(o.W3)&&_.unshift(o.W3),{columns:(0,a.Z)(_.filter((e=>""!==e)),i.Z),metrics:c===l.n.raw?void 0:(0,a.Z)(m,s.Z),orderby:p.length>0?p.map((e=>{if("string"===typeof e)try{return JSON.parse(e)}catch(e){throw new Error((0,r.t)("Found invalid orderby options"))}return e})):void 0}}},310581:(e,t,n)=>{n.d(t,{Z:()=>a});var r=n(472813);function a(e){return(0,r.s9)(e)?e:null!=e&&e.label?e.label:null==e?void 0:e.sqlExpression}},956652:(e,t,n)=>{n.d(t,{Z:()=>a});var r=n(62446);function a(e){return(0,r.AG)(e)?e:e.label?e.label:(0,r.nX)(e)?`${e.aggregate}(${e.column.columnName||e.column.column_name})`:e.sqlExpression}},111146:(e,t,n)=>{n.d(t,{Bw:()=>c,M8:()=>d,O6:()=>l,SR:()=>s});var r=n(472813),a=n(593185),o=n(5364),i=n(310581);const s=e=>(0,r.Gk)(e.x_axis),l=(0,a.c)(a.T.GENERIC_CHART_AXES),c=e=>{if(e.granularity_sqla||e.x_axis)return s(e)?e.x_axis:o.W3},d=e=>{const t=c(e);if(t)return(0,i.Z)(t)}},678444:(e,t,n)=>{n.d(t,{T:()=>s});var r=n(957557),a=n.n(r),o=n(472813),i=n(111146);function s(e,t){if(!(0,i.SR)(e))return t;const{columns:n,extras:r}=t,s=[...n||[]],l=null==n?void 0:n.findIndex((t=>(0,o.s9)(t)&&(0,o.s9)(e.x_axis)&&t===e.x_axis||(0,o.GA)(t)&&(0,o.GA)(e.x_axis)&&t.sqlExpression===e.x_axis.sqlExpression));if(void 0!==l&&l>-1&&e.x_axis&&Array.isArray(n)){(0,o.GA)(n[l])?s[l]={timeGrain:null==r?void 0:r.time_grain_sqla,columnType:"BASE_AXIS",...n[l]}:s[l]={timeGrain:null==r?void 0:r.time_grain_sqla,columnType:"BASE_AXIS",sqlExpression:e.x_axis,label:e.x_axis,expressionType:"SQL"};const i=a()(t,["extras.time_grain_sqla","is_timeseries"]);return i.columns=s,i}return t}},472813:(e,t,n)=>{function r(e){return"string"===typeof e}function a(e){return"string"!==typeof e&&void 0!==(null==e?void 0:e.sqlExpression)&&void 0!==(null==e?void 0:e.label)&&(void 0===(null==e?void 0:e.expressionType)||"SQL"===(null==e?void 0:e.expressionType))}function o(e){return r(e)||a(e)}n.d(t,{GA:()=>a,Gk:()=>o,ZP:()=>i,s9:()=>r});const i={}},46078:(e,t,n)=>{var r;n.d(t,{BH:()=>a,ZP:()=>o,i9:()=>r}),function(e){e.Table="table",e.Query="query",e.Dataset="dataset",e.SlTable="sl_table",e.SavedQuery="saved_query"}(r||(r={}));const a=[{metric_name:"COUNT(*)",expression:"COUNT(*)"}],o={}},46306:(e,t,n)=>{n.d(t,{Ki:()=>a,VK:()=>l,_l:()=>i,jz:()=>o,kC:()=>s});var r=n(631612);function a(e){return"SIMPLE"===e.expressionType}function o(e){return"SQL"===e.expressionType}function i(e){return(0,r.CW)(e.operator)}function s(e){return(0,r.VU)(e.operator)}function l(e){return(0,r.XA)(e.operator)}},62446:(e,t,n)=>{function r(e){return"string"!==typeof e&&!(null==e||!e.metric_name)}function a(e){return"string"===typeof e}function o(e){return"string"!==typeof e&&"SIMPLE"===(null==e?void 0:e.expressionType)}function i(e){return"string"!==typeof e&&"SQL"===(null==e?void 0:e.expressionType)}function s(e){return a(e)||o(e)||i(e)}n.d(t,{AG:()=>a,I0:()=>s,Ww:()=>r,ZP:()=>l,nX:()=>o,q5:()=>i});const l={}},631612:(e,t,n)=>{n.d(t,{CW:()=>a,VU:()=>i,XA:()=>l});const r=new Set(["IS NOT NULL","IS NULL"]);function a(e){return r.has(e)}const o=new Set(["==","!=",">","<",">=","<=","ILIKE","LIKE","REGEX","TEMPORAL_RANGE"]);function i(e){return o.has(e)}const s=new Set(["IN","NOT IN"]);function l(e){return s.has(e)}},920620:(e,t,n)=>{var r;n.d(t,{Z:()=>a,n:()=>r}),function(e){e.aggregate="aggregate",e.raw="raw"}(r||(r={}));const a={}},593185:(e,t,n)=>{var r;function a(e){try{return!!window.featureFlags[e]}catch(e){}return!1}n.d(t,{T:()=>r,c:()=>a}),function(e){e.ALERTS_ATTACH_REPORTS="ALERTS_ATTACH_REPORTS",e.ALERT_REPORTS="ALERT_REPORTS",e.ALLOW_DASHBOARD_DOMAIN_SHARDING="ALLOW_DASHBOARD_DOMAIN_SHARDING",e.ALLOW_FULL_CSV_EXPORT="ALLOW_FULL_CSV_EXPORT",e.CLIENT_CACHE="CLIENT_CACHE",e.DASHBOARD_CROSS_FILTERS="DASHBOARD_CROSS_FILTERS",e.DASHBOARD_EDIT_CHART_IN_NEW_TAB="DASHBOARD_EDIT_CHART_IN_NEW_TAB",e.DASHBOARD_FILTERS_EXPERIMENTAL="DASHBOARD_FILTERS_EXPERIMENTAL",e.CONFIRM_DASHBOARD_DIFF="CONFIRM_DASHBOARD_DIFF",e.DASHBOARD_DRILL_DOWN="DASHBOARD_DRILL_DOWN",e.DASHBOARD_NATIVE_FILTERS="DASHBOARD_NATIVE_FILTERS",e.DASHBOARD_NATIVE_FILTERS_SET="DASHBOARD_NATIVE_FILTERS_SET",e.DASHBOARD_VIRTUALIZATION="DASHBOARD_VIRTUALIZATION",e.DASHBOARD_RBAC="DASHBOARD_RBAC",e.DATAPANEL_CLOSED_BY_DEFAULT="DATAPANEL_CLOSED_BY_DEFAULT",e.DISABLE_DATASET_SOURCE_EDIT="DISABLE_DATASET_SOURCE_EDIT",e.DISABLE_LEGACY_DATASOURCE_EDITOR="DISABLE_LEGACY_DATASOURCE_EDITOR",e.DISPLAY_MARKDOWN_HTML="DISPLAY_MARKDOWN_HTML",e.DRILL_TO_DETAIL="DRILL_TO_DETAIL",e.DYNAMIC_PLUGINS="DYNAMIC_PLUGINS",e.EMBEDDABLE_CHARTS="EMBEDDABLE_CHARTS",e.EMBEDDED_SUPERSET="EMBEDDED_SUPERSET",e.ENABLE_ADVANCED_DATA_TYPES="ENABLE_ADVANCED_DATA_TYPES",e.ENABLE_DND_WITH_CLICK_UX="ENABLE_DND_WITH_CLICK_UX",e.ENABLE_EXPLORE_DRAG_AND_DROP="ENABLE_EXPLORE_DRAG_AND_DROP",e.ENABLE_FILTER_BOX_MIGRATION="ENABLE_FILTER_BOX_MIGRATION",e.ENABLE_JAVASCRIPT_CONTROLS="ENABLE_JAVASCRIPT_CONTROLS",e.ENABLE_TEMPLATE_PROCESSING="ENABLE_TEMPLATE_PROCESSING",e.ENABLE_TEMPLATE_REMOVE_FILTERS="ENABLE_TEMPLATE_REMOVE_FILTERS",e.ESCAPE_MARKDOWN_HTML="ESCAPE_MARKDOWN_HTML",e.ESTIMATE_QUERY_COST="ESTIMATE_QUERY_COST",e.FORCE_DATABASE_CONNECTIONS_SSL="FORCE_DATABASE_CONNECTIONS_SSL",e.GENERIC_CHART_AXES="GENERIC_CHART_AXES",e.GLOBAL_ASYNC_QUERIES="GLOBAL_ASYNC_QUERIES",e.HORIZONTAL_FILTER_BAR="HORIZONTAL_FILTER_BAR",e.LISTVIEWS_DEFAULT_CARD_VIEW="LISTVIEWS_DEFAULT_CARD_VIEW",e.SCHEDULED_QUERIES="SCHEDULED_QUERIES",e.SHARE_QUERIES_VIA_KV_STORE="SHARE_QUERIES_VIA_KV_STORE",e.SQLLAB_BACKEND_PERSISTENCE="SQLLAB_BACKEND_PERSISTENCE",e.SQL_VALIDATORS_BY_ENGINE="SQL_VALIDATORS_BY_ENGINE",e.THUMBNAILS="THUMBNAILS",e.USE_ANALAGOUS_COLORS="USE_ANALAGOUS_COLORS",e.UX_BETA="UX_BETA",e.VERSIONED_EXPORT="VERSIONED_EXPORT",e.SSH_TUNNELING="SSH_TUNNELING"}(r||(r={}))},237731:(e,t,n)=>{function r(e){return null!==e&&void 0!==e}n.d(t,{Z:()=>r})},274765:(e,t,n)=>{n.d(t,{Z:()=>r});const r=function(e,t){if(t){const n=new Set;return e.filter((e=>{const r=t(e);return!n.has(r)&&(n.add(r),!0)}))}return[...new Set(e)]}},941331:(e,t,n)=>{n.d(t,{W:()=>Z});var r=n(441609),a=n.n(r),o=n(150361),i=n.n(o),s=n(667294),l=n(730381),c=n.n(l),d=n(828216),u=n(748086),_=n(970553),m=n(287183),p=n(49937),E=n(9875),g=n(774069),h=n(835932),f=n(751995),A=n(431069),T=n(455867);var S;!function(e){e[e.SAVE_NEW=1]="SAVE_NEW",e[e.OVERWRITE_DATASET=2]="OVERWRITE_DATASET"}(S||(S={}));const b={metrics:[],groupby:[],time_range:"No filter",row_limit:1e3};var N=n(112515),y=n(340219),v=n(427600),I=n(667496),R=n(211965);const O=f.iK.div`
  .sdm-body {
    margin: 0 8px;
  }
  .sdm-input {
    margin-left: 45px;
    width: 401px;
  }
  .sdm-autocomplete {
    width: 401px;
    align-self: center;
  }
  .sdm-radio {
    display: block;
    height: 30px;
    margin: 10px 0px;
    line-height: 30px;
  }
  .sdm-overwrite-msg {
    margin: 7px;
  }
  .sdm-overwrite-container {
    flex: 1 1 auto;
    display: flex;
  }
`,L={adddev_menu:"\u65b0\u5efa\u76ee\u5f55",adddev_name:"\u76ee\u5f55\u540d\u79f0",pid:""};let D={...L};const x=async(e,t,n,r,a,o)=>{const i=`api/v1/dataset/${t}?override_columns=${o}`,s=JSON.stringify({sql:n,columns:r,owners:a,database_id:e});return(await A.Z.put({endpoint:i,headers:{"Content-Type":"application/json"},body:s})).json.result},w=(0,T.t)("Untitled Dataset"),Z=({visible:e,onHide:t,buttonTextOnSave:n,buttonTextOnOverwrite:r,modalDescription:o,datasource:l,openWindow:f=!0,formData:Z={},issavedatasetbtn:C})=>{const U=(0,d.v9)((e=>{var t,n;return(null==(t=e.common)||null==(n=t.conf)?void 0:n.DEFAULT_VIZ_TYPE)||"table"})),$=l;(0,s.useEffect)((()=>{let e=`${$.tab} ${c()().format("MM/DD/YYYY HH:mm:ss")}`;F(e)}),[$]);const P=C;(0,s.useEffect)((()=>{"yes"==P?A.Z.get({endpoint:"/api/v2/dataset/group/"}).then((e=>{if(200==e.json.meta.code||201==e.json.meta.code){const t=se(i()(e.json.meta.data),"");M(t)}else u.ZP.error(e.json.meta.message),M([])})):A.Z.get({endpoint:"/api/v2/dataset/group/tree/"}).then((e=>{if(200==e.json.meta.code||201==e.json.meta.code){const t=se(i()(e.json.meta.data),"");k(t)}else u.ZP.error(e.json.meta.message),k([])}))}),[P]),(0,s.useEffect)((()=>{oe("")}),[]);const[B,M]=(0,s.useState)([]),[H,k]=(0,s.useState)([]),G=()=>`${(null==l?void 0:l.name)||w} ${c()().format("MM/DD/YYYY HH:mm:ss")}`,[W,F]=(0,s.useState)(G()),[V,q]=(0,s.useState)(S.SAVE_NEW),[z,K]=(0,s.useState)(!1),[j,Y]=(0,s.useState)({}),[X,Q]=(0,s.useState)(void 0),J=(0,d.v9)((e=>(e=>{if(e.hasOwnProperty("sqlLab")){const{sqlLab:{user:t}}=e;return t}const{user:t}=e;return t})(e))),[ee,te]=(0,s.useState)({label:null,value:null}),ne=e=>{f?window.open(e,"_blank","noreferrer"):window.location.href=e},re={...b,...Z||{}},ae=(0,s.useCallback)((async(e="")=>A.Z.get({endpoint:`/api/v2/dataset/?name=${e}&database_id=${$.dbId.toString()}&schema=${$.schema}`}).then((e=>({data:e.json.meta.data.map((e=>({value:e.id,label:e.custom_name?e.custom_name:e.table_name,datasetid:e.id,owners:e.owners})))})))),[J]),oe=async(e="")=>{const{userId:t}=J;t&&await A.Z.get({endpoint:`/api/v2/dataset/?name=${e}`}).then((e=>{let t=[];200!=e.json.meta.code&&201!=e.json.meta.code||e.json.meta.data.map((e=>{let n={value:e.id,label:e.custom_name?e.custom_name:e.table_name,datasetid:e.id,owners:e.owners};t.push(n)}))}))},ie=V===S.SAVE_NEW&&0===W.length||V===S.OVERWRITE_DATASET&&a()(X);function se(e,t){const n=[];return e.forEach((e=>{const r={title:e.name,allname:`${t?t+"-":""}${e.name}`,key:e.group_id,value:e.group_id,disabled:e.perm<4,children:se(e.children,e.name)};(!r.disabled||r.children.length>0)&&n.push(r)})),n}const le=(e,t)=>{let n={},r=(e,a)=>{e.map((e=>{e.value==a&&(n={label:e.allname,value:e.value}),e.children.length>0&&r(e.children,t)}))};return r(e,t),n};return(0,R.tZ)(g.Z,{show:e,title:(0,T.t)("Save or Overwrite Dataset"),onHide:t,footer:(0,R.tZ)(s.Fragment,null,V===S.SAVE_NEW&&(0,R.tZ)(h.Z,{disabled:ie,buttonStyle:"primary",onClick:()=>{if(V===S.OVERWRITE_DATASET)return void K(!0);if(""==D.pid||null==D.pid)return u.ZP.error((0,T.t)("Please select a group"));const e=$.results&&$.results.selected_columns||[];if($.templateParams){const e=JSON.parse($.templateParams);e._filters&&(delete e._filters,$.templateParams=JSON.stringify(e))}const n={schema:$.schema,sql:$.sql,database_id:$.dbId.toString(),table_name:W,columns:e,table_group_id:D.pid.toString()};return A.Z.post({endpoint:"/api/v2/dataset/sqllab_viz/",body:JSON.stringify(n),headers:{"Content-Type":"application/json"}}).then((async e=>{if(200==e.json.meta.code||201==e.json.meta.code)if(u.ZP.success(e.json.meta.message),"yes"==P){sessionStorage.setItem("sqldatabaseid",e.json.meta.data.id),sessionStorage.setItem("key",e.json.meta.data.id);const t=[],n=e=>{if(e&&e.length)return e.some((e=>{if(`${e.value}`===D.pid.toString())return t.unshift(`${e.value}`),!0;if(e.children&&e.children.length){t.unshift(`${e.value}`);const r=n(e.children);return r||t.shift(),r}}))};n("yes"==P?B:H),sessionStorage.setItem("keyPath",JSON.stringify(t)),window.location.href=(0,I.VU)("/tablemodelview/list/")}else{t();const n=await(0,y.nv)(e.json.meta.data.id,"table",{...re,datasource:`${e.json.meta.data.id}__table`,viz_type:"table",all_columns:$.columns.map((e=>e.name))}),r=(0,N.y8)(null,{[v.KD.formDataKey.name]:n});ne(r)}else u.ZP.error(e.json.meta.message)}))}},n),V===S.OVERWRITE_DATASET&&(0,R.tZ)(s.Fragment,null,z&&(0,R.tZ)(h.Z,{onClick:()=>{K(!1)}},(0,T.t)("Back")),(0,R.tZ)(h.Z,{className:"md",buttonStyle:"primary",onClick:async()=>{var e,n;if(!z)return void K(!0);const[,r]=await Promise.all([x(null==l?void 0:l.dbId,null==j?void 0:j.datasetid,null==l?void 0:l.sql,null==l||null==(e=l.columns)?void 0:e.map((e=>({column_name:e.name,type:e.type,is_dttm:e.is_dttm}))),[],!0),(0,y.nv)(j.datasetid,"table",{...re,datasource:`${j.datasetid}__table`,..."table"===U&&{all_columns:null==l||null==(n=l.columns)?void 0:n.map((e=>e.name))}})]);if("yes"==P)u.ZP.success((0,T.t)("success")),sessionStorage.setItem("sqldatabaseid",j.datasetid),window.location.href="/tablemodelview/list/";else{u.ZP.success((0,T.t)("success"));const e=(0,N.y8)(null,{[v.KD.formDataKey.name]:r});ne(e)}K(!1),F(G()),t()},disabled:ie},r)))},(0,R.tZ)(O,null,!z&&(0,R.tZ)("div",{className:"sdm-body"},o&&(0,R.tZ)("div",{className:"sdm-prompt"},o),(0,R.tZ)(m.Y.Group,{onChange:e=>{q(Number(e.target.value))},value:V},(0,R.tZ)(m.Y,{className:"sdm-radio",value:1},(0,T.t)("Save as new"),(0,R.tZ)(E.II,{className:"sdm-input",value:W,onChange:e=>{F(e.target.value)},disabled:1!==V})),(0,R.tZ)("div",{className:"Radio-Tree"},(0,R.tZ)("label",null,(0,T.t)("Select Group")),(0,R.tZ)(_.Z,{disabled:1!==V,labelInValue:!0,showSearch:!0,style:{width:"401px",marginLeft:"18px"},value:ee,dropdownStyle:{maxHeight:400,overflow:"auto"},placeholder:(0,T.t)("Please select"),onChange:function(e,t){let n={};n=le("yes"==P?B:H,e.value),te(n),D={...L,pid:e.value}},treeData:"yes"==P?B:H,treeNodeFilterProp:"title"})),(0,R.tZ)("div",{className:"sdm-overwrite-container"},(0,R.tZ)(m.Y,{className:"sdm-radio",value:2},(0,T.t)("Overwrite existing")),(0,R.tZ)("div",{className:"sdm-autocomplete"},(0,R.tZ)(p.qb,{allowClear:!0,showSearch:!0,placeholder:(0,T.t)("Select or type dataset name"),ariaLabel:(0,T.t)("Existing dataset"),onChange:(e,t)=>{Y(t),Q(e)},options:e=>ae(e),value:X,disabled:2!==V,getPopupContainer:()=>document.body}))))),z&&(0,R.tZ)("div",{className:"sdm-overwrite-msg"},(0,T.t)("Are you sure you want to overwrite this dataset?"))))}},444904:(e,t,n)=>{n.d(t,{Em:()=>i,GJ:()=>v,IY:()=>a,N2:()=>N,OI:()=>O,TU:()=>A,U$:()=>T,Yn:()=>y,Yo:()=>f,b$:()=>S,bR:()=>s,eU:()=>l,ev:()=>c,fM:()=>E,hC:()=>g,iJ:()=>I,lV:()=>p,lr:()=>R,oN:()=>m,rD:()=>b,rP:()=>u,rp:()=>d,uC:()=>o,xj:()=>_,zY:()=>h});var r=n(455867);const a={offline:"danger",failed:"danger",pending:"info",fetching:"info",running:"warning",stopped:"danger",success:"success"},o={offline:(0,r.t)("offline"),failed:(0,r.t)("failed"),pending:(0,r.t)("pending"),fetching:(0,r.t)("fetching"),running:(0,r.t)("running"),stopped:(0,r.t)("stopped"),success:(0,r.t)("success")},i={success:"success",failed:"failed",running:"running",offline:"offline",pending:"pending"},s={success:(0,r.t)("success"),failed:(0,r.t)("failed"),running:(0,r.t)("running"),offline:(0,r.t)("offline"),pending:(0,r.t)("pending")},l=5,c=3,d=51,u=400,_=10,m=30,p=70,E=2e3,g=600,h=100,f=1024,A=2,T=864e5,S=5120,b=.9,N=8e3,y=100,v=90,I=60,R=55,O=50},233313:(e,t,n)=>{n.d(t,{Z:()=>a});var r=n(444904);const a=["AND","AS","ASC","AVG","BY","CASE","COUNT","CREATE","CROSS","DATABASE","DEFAULT","DELETE","DESC","DISTINCT","DROP","ELSE","END","FOREIGN","FROM","GRANT","GROUP","HAVING","IF","INNER","INSERT","JOIN","KEY","LEFT","LIMIT","MAX","MIN","NATURAL","NOT","NULL","OFFSET","ON","OR","ORDER","OUTER","PRIMARY","REFERENCES","RIGHT","SELECT","SUM","TABLE","THEN","TYPE","UNION","UPDATE","WHEN","WHERE"].concat(["BIGINT","BINARY","BIT","CHAR","DATE","DECIMAL","DOUBLE","FLOAT","INT","INTEGER","MONEY","NUMBER","NUMERIC","REAL","SET","TEXT","TIMESTAMP","VARCHAR"]).map((e=>({meta:"sql",name:e,score:r.Yn,value:e})))},229487:(e,t,n)=>{n.d(t,{Z:()=>c});var r=n(205872),a=n.n(r),o=n(211965),i=(n(667294),n(404863)),s=n(751995),l=n(731293);function c(e){const{type:t="info",description:n,showIcon:r=!0,closable:c=!0,roomBelow:d=!1,children:u}=e,_=(0,s.Fg)(),{colors:m,typography:p,gridUnit:E}=_,{alert:g,error:h,info:f,success:A}=m;let T=f,S=l.Z.InfoSolid;return"error"===t?(T=h,S=l.Z.ErrorSolid):"warning"===t?(T=g,S=l.Z.AlertSolid):"success"===t&&(T=A,S=l.Z.CircleCheckSolid),(0,o.tZ)(i.default,a()({role:"alert",showIcon:r,icon:(0,o.tZ)(S,{"aria-label":`${t} icon`}),closeText:c&&(0,o.tZ)(l.Z.XSmall,{"aria-label":"close icon"}),css:(0,o.iv)({marginBottom:d?4*E:0,padding:`${2*E}px ${3*E}px`,alignItems:"flex-start",border:0,backgroundColor:T.light2,"& .ant-alert-icon":{marginRight:2*E},"& .ant-alert-message":{color:T.dark2,fontSize:p.sizes.m,fontWeight:n?p.weights.bold:p.weights.normal},"& .ant-alert-description":{color:T.dark2,fontSize:p.sizes.m}},"","")},e),u)}},794670:(e,t,n)=>{n.d(t,{Ad:()=>g,YH:()=>p,Z5:()=>h,cE:()=>m,iO:()=>u,ry:()=>E,up:()=>_});var r=n(205872),a=n.n(r),o=n(667294),i=n(953239),s=n(967913),l=n(211965);const c={"mode/sql":()=>n.e(48883).then(n.t.bind(n,248883,23)),"mode/markdown":()=>Promise.all([n.e(39794),n.e(95802),n.e(94832),n.e(66061)]).then(n.t.bind(n,866061,23)),"mode/css":()=>Promise.all([n.e(95802),n.e(94972)]).then(n.t.bind(n,994972,23)),"mode/json":()=>n.e(58750).then(n.t.bind(n,158750,23)),"mode/yaml":()=>n.e(60741).then(n.t.bind(n,260741,23)),"mode/html":()=>Promise.all([n.e(39794),n.e(95802),n.e(94832),n.e(71258)]).then(n.t.bind(n,171258,23)),"mode/javascript":()=>Promise.all([n.e(39794),n.e(54579)]).then(n.t.bind(n,754579,23)),"theme/textmate":()=>n.e(2089).then(n.t.bind(n,302089,23)),"theme/github":()=>n.e(50440).then(n.t.bind(n,550440,23)),"ext/language_tools":()=>n.e(75335).then(n.t.bind(n,375335,23)),"ext/searchbox":()=>n.e(68656).then(n.t.bind(n,468656,23))};function d(e,{defaultMode:t,defaultTheme:r,defaultTabSize:d=2,placeholder:u}={}){return(0,s.Z)((async()=>{var s,u;const{default:_}=await n.e(74981).then(n.bind(n,874981));await Promise.all(e.map((e=>c[e]())));const m=t||(null==(s=e.find((e=>e.startsWith("mode/"))))?void 0:s.replace("mode/","")),p=r||(null==(u=e.find((e=>e.startsWith("theme/"))))?void 0:u.replace("theme/",""));return(0,o.forwardRef)((function({keywords:e,mode:t=m,theme:n=p,tabSize:r=d,defaultValue:o="",...s},c){if(e){const n={getCompletions:(n,r,a,o,i)=>{Number.isNaN(parseInt(o,10))&&r.getMode().$id===`ace/mode/${t}`&&i(null,e)}};(0,i.acequire)("ace/ext/language_tools").setCompleters([n])}return(0,l.tZ)(_,a()({ref:c,mode:t,theme:n,tabSize:r,defaultValue:o},s))}))}),u)}const u=d(["mode/sql","theme/github","ext/language_tools","ext/searchbox"]),_=d(["mode/sql","theme/github","ext/language_tools","ext/searchbox"],{placeholder:()=>(0,l.tZ)("div",{style:{height:"100%"}},(0,l.tZ)("div",{style:{width:41,height:"100%",background:"#e8e8e8"}}),(0,l.tZ)("div",{className:"ace_content"}))}),m=d(["mode/markdown","theme/textmate"]),p=d(["mode/markdown","mode/sql","mode/json","mode/html","mode/javascript","theme/textmate"]),E=d(["mode/css","theme/github"]),g=d(["mode/json","theme/github"]),h=d(["mode/json","mode/yaml","theme/github"])},967913:(e,t,n)=>{n.d(t,{Z:()=>c});var r=n(205872),a=n.n(r),o=n(667294),i=n(838703),s=n(211965);function l({width:e,height:t,showLoadingForImport:n=!1,placeholderStyle:r}){return t&&(0,s.tZ)("div",{key:"async-asm-placeholder",style:{width:e,height:t,...r}},n&&(0,s.tZ)(i.Z,{position:"floating"}))||null}function c(e,t=l){let n,r;function i(){return n||(n=e instanceof Promise?e:e()),r||n.then((e=>{r=e.default||e})),n}const c=(0,o.forwardRef)((function(e,n){const[l,c]=(0,o.useState)(void 0!==r);(0,o.useEffect)((()=>{let e=!0;return l||i().then((()=>{e&&c(!0)})),()=>{e=!1}}));const d=r||t;return d?(0,s.tZ)(d,a()({ref:d===r?n:null},e)):null}));return c.preload=i,c}},843700:(e,t,n)=>{n.d(t,{Z:()=>i});n(667294);var r=n(751995),a=n(427279),o=n(211965);const i=Object.assign((0,r.iK)((({light:e,bigger:t,bold:n,animateArrows:r,...i})=>(0,o.tZ)(a.Z,i)))`
    .ant-collapse-item {
      .ant-collapse-header {
        font-weight: ${({bold:e,theme:t})=>e?t.typography.weights.bold:t.typography.weights.normal};
        font-size: ${({bigger:e,theme:t})=>e?4*t.gridUnit+"px":"inherit"};

        .ant-collapse-arrow svg {
          transition: ${({animateArrows:e})=>e?"transform 0.24s":"none"};
        }

        ${({expandIconPosition:e})=>e&&"right"===e&&"\n            .anticon.anticon-right.ant-collapse-arrow > svg {\n              transform: rotate(90deg) !important;\n            }\n          "}

        ${({light:e,theme:t})=>e&&`\n            color: ${t.colors.grayscale.light4};\n            .ant-collapse-arrow svg {\n              color: ${t.colors.grayscale.light4};\n            }\n          `}

        ${({ghost:e,bordered:t,theme:n})=>e&&t&&`\n            border-bottom: 1px solid ${n.colors.grayscale.light3};\n          `}
      }
      .ant-collapse-content {
        .ant-collapse-content-box {
          .loading.inline {
            margin: ${({theme:e})=>12*e.gridUnit}px auto;
            display: block;
          }
        }
      }
    }
    .ant-collapse-item-active {
      .ant-collapse-header {
        ${({expandIconPosition:e})=>e&&"right"===e&&"\n            .anticon.anticon-right.ant-collapse-arrow > svg {\n              transform: rotate(-90deg) !important;\n            }\n          "}
      }
    }
  `,{Panel:a.Z.Panel})},94301:(e,t,n)=>{n.d(t,{Tc:()=>y,UX:()=>I,XJ:()=>b,x3:()=>N});n(667294);var r,a=n(751995),o=n(211965),i=n(455867),s=n(667496),l=n(49937),c=n(835932);!function(e){e[e.Small=0]="Small",e[e.Medium=1]="Medium",e[e.Big=2]="Big"}(r||(r={}));const d=a.iK.div`
  ${({theme:e})=>o.iv`
    display: flex;
    flex-direction: column;
    width: 100%;
    align-items: center;
    justify-content: center;
    padding: ${4*e.gridUnit}px;
    text-align: center;
    //height:80vh;
    & .ant-empty-image svg {
      width: auto;
    }

    & a,
    & span[role='button'] {
      color: inherit;
      text-decoration: underline;
      &:hover {
        color: ${e.colors.grayscale.base};
      }
    }
  `}
`,u=a.iK.div``,_=a.iK.p`
  ${({theme:e})=>o.iv`
    font-size: ${e.typography.sizes.m}px;
    color: ${e.colors.grayscale.light1};
    margin: ${2*e.gridUnit}px 0 0 0;
    font-weight: ${e.typography.weights.bold};
  `}
`,m=(0,a.iK)(_)`
  ${({theme:e})=>o.iv`
    font-size: ${e.typography.sizes.l}px;
    color: ${e.colors.grayscale.light1};
    margin-top: ${4*e.gridUnit}px;
  `}
`,p=a.iK.p`
  ${({theme:e})=>o.iv`
    font-size: ${e.typography.sizes.s}px;
    color: ${e.colors.grayscale.light1};
    margin: ${2*e.gridUnit}px 0 0 0;
  `}
`,E=(0,a.iK)(p)`
  ${({theme:e})=>o.iv`
    font-size: ${e.typography.sizes.m}px;
  `}
`,g=(0,a.iK)(p)`
  ${({theme:e})=>o.iv`
    margin-top: ${e.gridUnit}px;
    line-height: 1.2;
  `}
`,h=(0,a.iK)(c.Z)`
  ${({theme:e})=>o.iv`
    margin-top: ${4*e.gridUnit}px;
    z-index: 1;
  `}
`,f=e=>"string"===typeof e?(0,s.VU)(`/static/assets/images/${e}`):e,A=e=>{switch(e){case r.Small:return{height:"50px"};case r.Medium:return{height:"80px"};case r.Big:return{height:"150px"};default:return{height:"50px"}}},T=({image:e,size:t})=>(0,o.tZ)(l.HY,{description:!1,image:f(e),imageStyle:A(t)}),S=e=>{e.preventDefault(),e.stopPropagation()},b=({title:e,image:t,description:n,buttonAction:a,buttonText:i,className:s})=>(0,o.tZ)(d,{className:s,style:{position:"absolute",zIndex:10,marginTop:"20px"}},t&&(0,o.tZ)(T,{image:t,size:r.Big}),(0,o.tZ)(u,{css:e=>o.iv`
          max-width: ${150*e.gridUnit}px;
        `},(0,o.tZ)(m,null,e),n&&(0,o.tZ)(E,null,n),a&&i&&(0,o.tZ)(h,{buttonStyle:"primary",onClick:a,onMouseDown:S},i))),N=({title:e,image:t,description:n,buttonAction:a,buttonText:i,containerStyle:s})=>(0,o.tZ)(d,{style:s},t&&(0,o.tZ)(T,{image:t,size:r.Medium}),(0,o.tZ)(u,{css:e=>o.iv`
          max-width: ${100*e.gridUnit}px;
        `},(0,o.tZ)(_,null,e),n&&(0,o.tZ)(p,null,n),i&&a&&(0,o.tZ)(h,{buttonStyle:"primary",onClick:a,onMouseDown:S},i))),y=({title:e,image:t,description:n})=>(0,o.tZ)(d,null,t&&(0,o.tZ)(T,{image:t,size:r.Small}),(0,o.tZ)(u,{css:e=>o.iv`
          max-width: ${75*e.gridUnit}px;
        `},(0,o.tZ)(_,null,e),n&&(0,o.tZ)(g,null,n))),v={NO_DATABASES_MATCH_TITLE:(0,i.t)("No databases match your search"),NO_DATABASES_AVAILABLE_TITLE:(0,i.t)("There are no databases available"),MANAGE_YOUR_DATABASES_TEXT:(0,i.t)("Manage your databases"),HERE_TEXT:(0,i.t)("here")},I=e=>(0,o.tZ)(y,{image:"empty.svg",title:e?v.NO_DATABASES_MATCH_TITLE:v.NO_DATABASES_AVAILABLE_TITLE,description:(0,o.tZ)("p",null,v.MANAGE_YOUR_DATABASES_TEXT," ",(0,o.tZ)("a",{href:(0,s.VU)("/databaseview/list")},v.HERE_TEXT))})},272875:(e,t,n)=>{n.d(t,{Z:()=>c});var r=n(667294),a=n(455867),o=n(792869),i=n(891178),s=n(211965);const l=(0,a.t)("Unexpected error");function c({title:e=l,error:t,subtitle:n,copyText:a,link:c,stackTrace:d,source:u,description:_}){if(t){const e=(0,o.Z)().get(t.error_type);if(e)return(0,s.tZ)(e,{error:t,source:u,subtitle:n})}return(0,s.tZ)(i.Z,{level:"warning",title:e,subtitle:n,copyText:a,description:_,source:u,body:c||d?(0,s.tZ)(r.Fragment,null,c&&(0,s.tZ)("a",{href:c,target:"_blank",rel:"noopener noreferrer"},"(Request Access)"),(0,s.tZ)("br",null),d&&(0,s.tZ)("pre",null,d)):void 0})}},804591:(e,t,n)=>{n.d(t,{Z:()=>a});var r=n(897538);const a=(0,n(751995).iK)(r.Z.Item)`
  ${({theme:e})=>`\n    .ant-form-item-label {\n      padding-bottom: ${e.gridUnit}px;\n      & > label {\n        text-transform: uppercase;\n        font-size: ${e.typography.sizes.s}px;\n        color: ${e.colors.grayscale.base};\n\n        &.ant-form-item-required:not(.ant-form-item-required-mark-optional) {\n          &::before {\n            display: none;\n          }\n          &::after {\n            display: inline-block;\n            color: ${e.colors.error.base};\n            font-size: ${e.typography.sizes.s}px;\n            content: '*';\n          }\n        }\n      }\n    }\n  `}
`},902857:(e,t,n)=>{n.d(t,{Z:()=>s});n(667294);var r=n(751995),a=n(211965);const o=r.iK.label`
  text-transform: uppercase;
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
  color: ${({theme:e})=>e.colors.grayscale.base};
  margin-bottom: ${({theme:e})=>e.gridUnit}px;
`,i=r.iK.label`
  text-transform: uppercase;
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
  color: ${({theme:e})=>e.colors.grayscale.base};
  margin-bottom: ${({theme:e})=>e.gridUnit}px;
  &::after {
    display: inline-block;
    margin-left: ${({theme:e})=>e.gridUnit}px;
    color: ${({theme:e})=>e.colors.error.base};
    font-size: ${({theme:e})=>e.typography.sizes.m}px;
    content: '*';
  }
`;function s({children:e,htmlFor:t,required:n=!1,className:r}){const s=n?i:o;return(0,a.tZ)(s,{htmlFor:t,className:r},e)}},84367:(e,t,n)=>{n.d(t,{Z:()=>y});var r,a=n(205872),o=n.n(a),i=n(667294),s=n(432787),l=n(931097),c=n(751995),d=n(211965),u=n(455867),_=n(608272),m=n(731293);function p(){return p=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var r in n)Object.prototype.hasOwnProperty.call(n,r)&&(e[r]=n[r])}return e},p.apply(this,arguments)}const E=function(e){return i.createElement("svg",p({width:24,height:24,viewBox:"0 0 24 24",fill:"none",xmlns:"http://www.w3.org/2000/svg"},e),r||(r=i.createElement("path",{fillRule:"evenodd",clipRule:"evenodd",d:"M12 7a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1zm0 8a1 1 0 100 2 1 1 0 000-2zm9.71-7.44l-5.27-5.27a1.05 1.05 0 00-.71-.29H8.27a1.05 1.05 0 00-.71.29L2.29 7.56a1.05 1.05 0 00-.29.71v7.46c.004.265.107.518.29.71l5.27 5.27c.192.183.445.286.71.29h7.46a1.05 1.05 0 00.71-.29l5.27-5.27a1.05 1.05 0 00.29-.71V8.27a1.05 1.05 0 00-.29-.71zM20 15.31L15.31 20H8.69L4 15.31V8.69L8.69 4h6.62L20 8.69v6.62z",fill:"currentColor"})))};var g=n(804591),h=n(902857);const f=(0,c.iK)(s.Z)`
  margin: ${({theme:e})=>`${e.gridUnit}px 0 ${2*e.gridUnit}px`};
`,A=(0,c.iK)(s.Z.Password)`
  margin: ${({theme:e})=>`${e.gridUnit}px 0 ${2*e.gridUnit}px`};
`,T=(0,c.iK)("div")`
  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
  margin-bottom: ${({theme:e})=>3*e.gridUnit}px;
  .ant-form-item {
    margin-bottom: 0;
  }
`,S=c.iK.div`
  display: flex;
  align-items: center;
`,b=(0,c.iK)(h.Z)`
  margin-bottom: 0;
`,N=d.iv`
  &.anticon > * {
    line-height: 0;
  }
`,y=({label:e,validationMethods:t,errorMessage:n,helpText:r,required:a=!1,hasTooltip:i=!1,tooltipText:s,id:c,className:p,visibilityToggle:h,...y})=>(0,d.tZ)(T,{className:p},(0,d.tZ)(S,null,(0,d.tZ)(b,{htmlFor:c,required:a},e),i&&(0,d.tZ)(_.Z,{tooltip:`${s}`,viewBox:"0 -1 24 24"})),(0,d.tZ)(g.Z,{css:e=>((e,t)=>d.iv`
  .ant-form-item-children-icon {
    display: none;
  }
  ${t&&`.ant-form-item-control-input-content {\n      position: relative;\n      &:after {\n        content: ' ';\n        display: inline-block;\n        background: ${e.colors.error.base};\n        mask: url(${E});\n        mask-size: cover;\n        width: ${4*e.gridUnit}px;\n        height: ${4*e.gridUnit}px;\n        position: absolute;\n        right: ${1.25*e.gridUnit}px;\n        top: ${2.75*e.gridUnit}px;\n      }\n    }`}
`)(e,!!n),validateTrigger:Object.keys(t),validateStatus:n?"error":"success",help:n||r,hasFeedback:!!n},h||"password"===y.name?(0,d.tZ)(A,o()({},y,t,{iconRender:e=>e?(0,d.tZ)(l.Z,{title:(0,u.t)("Hide password.")},(0,d.tZ)(m.Z.EyeInvisibleOutlined,{iconSize:"m",css:N})):(0,d.tZ)(l.Z,{title:(0,u.t)("Show password.")},(0,d.tZ)(m.Z.EyeOutlined,{iconSize:"m",css:N,"data-test":"icon-eye"})),role:"textbox"})):(0,d.tZ)(f,o()({},y,t))))},49238:(e,t,n)=>{n.d(t,{l0:()=>s,xJ:()=>l.Z,lX:()=>c.Z});n(667294);var r=n(897538),a=n(751995),o=n(211965);const i=(0,a.iK)(r.Z)`
  &.ant-form label {
    font-size: ${({theme:e})=>e.typography.sizes.s}px;
  }
  .ant-form-item {
    margin-bottom: ${({theme:e})=>4*e.gridUnit}px;
  }
`;function s(e){return(0,o.tZ)(i,e)}var l=n(804591),c=n(902857);n(84367)},608272:(e,t,n)=>{n.d(t,{Z:()=>u});n(667294);var r=n(751995),a=n(358593),o=n(731293),i=n(211965);const s=(0,r.iK)(a.u)`
  cursor: pointer;
  path:first-of-type {
    fill: ${({theme:e})=>e.colors.grayscale.base};
  }
`,l=r.iK.span`
  display: -webkit-box;
  -webkit-line-clamp: 20;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
`,c={fontSize:"12px",lineHeight:"16px"},d="rgba(0,0,0,0.9)";function u({tooltip:e,placement:t="right",trigger:n="hover",overlayStyle:r=c,bgColor:a=d,viewBox:u="0 -2 24 24"}){return(0,i.tZ)(s,{title:(0,i.tZ)(l,null,e),placement:t,trigger:n,overlayStyle:r,color:a},(0,i.tZ)(o.Z.InfoSolidSmall,{className:"info-solid-small",viewBox:u}))}},9875:(e,t,n)=>{n.d(t,{II:()=>i,Kx:()=>l,Rn:()=>s});var r=n(751995),a=n(432787),o=n(624225);const i=(0,r.iK)(a.Z)`
  border: 1px solid ${({theme:e})=>e.colors.secondary.light3};
  border-radius: ${({theme:e})=>e.borderRadius}px;
`,s=(0,r.iK)(o.Z)`
  border: 1px solid ${({theme:e})=>e.colors.secondary.light3};
  border-radius: ${({theme:e})=>e.borderRadius}px;
`,l=(0,r.iK)(a.Z.TextArea)`
  border: 1px solid ${({theme:e})=>e.colors.secondary.light3};
  border-radius: ${({theme:e})=>e.borderRadius}px;
`},737921:(e,t,n)=>{n.d(t,{Z:()=>l});var r=n(205872),a=n.n(r),o=n(211965),i=(n(667294),n(49937)),s=n(751995);function l(e){const t=(0,s.Fg)(),{colors:n,transitionTiming:r}=t,{type:l="default",onClick:c,children:d,...u}=e,{alert:_,primary:m,secondary:p,grayscale:E,success:g,warning:h,error:f,info:A}=n;let T=E.light3,S=c?m.light2:E.light3,b=c?E.light2:"transparent",N=c?m.light1:"transparent",y=E.dark1;if("default"!==l){let e;y=E.light4,"alert"===l?(y=E.dark1,e=_):e="success"===l?g:"warning"===l?h:"danger"===l?f:"info"===l?A:"secondary"===l?p:m,T=e.base,S=c?e.dark1:e.base,b=c?e.dark1:"transparent",N=c?e.dark2:"transparent"}return(0,o.tZ)(i.Vp,a()({onClick:c},u,{css:(0,o.iv)({transition:`background-color ${r}s`,whiteSpace:"nowrap",cursor:c?"pointer":"default",overflow:"hidden",textOverflow:"ellipsis",backgroundColor:T,borderColor:b,borderRadius:21,padding:"0.35em 0.8em",lineHeight:1,color:y,maxWidth:"100%","&:hover":{backgroundColor:S,borderColor:N,opacity:1}},"","")}),d)}},683862:(e,t,n)=>{n.d(t,{$t:()=>u,Rh:()=>_,v2:()=>d});var r=n(751995),a=n(99210),o=n(997183),i=n(454076);const s=(0,r.iK)(a.Z.Item)`
  > a {
    text-decoration: none;
  }

  &.ant-menu-item {
    height: ${({theme:e})=>8*e.gridUnit}px;
    line-height: ${({theme:e})=>8*e.gridUnit}px;
    a {
      border-bottom: none;
      transition: background-color ${({theme:e})=>e.transitionTiming}s;
      &:after {
        content: '';
        position: absolute;
        bottom: -3px;
        left: 50%;
        width: 0;
        height: 3px;
        opacity: 0;
        transform: translateX(-50%);
        transition: all ${({theme:e})=>e.transitionTiming}s;
        background-color: ${({theme:e})=>e.colors.primary.base};
      }
      &:focus {
        border-bottom: none;
        background-color: transparent;
        @media (max-width: 767px) {
          background-color: ${({theme:e})=>e.colors.primary.light5};
        }
      }
    }
  }

  &.ant-menu-item,
  &.ant-dropdown-menu-item {
    span[role='button'] {
      display: inline-block;
      width: 100%;
    }
    transition-duration: 0s;
  }
`,l=(0,r.iK)(a.Z)`
  border: none;

  & > .ant-menu-item,
  & > .ant-menu-submenu {
    vertical-align: inherit;
    &:hover {
      color: ${({theme:e})=>e.colors.grayscale.dark1};
    }
  }

  &:not(.ant-menu-dark) > .ant-menu-submenu,
  &:not(.ant-menu-dark) > .ant-menu-item {
    &:hover {
      border-bottom: none;
    }
  }

  &:not(.ant-menu-dark) > .ant-menu-submenu,
  &:not(.ant-menu-dark) > .ant-menu-item {
    margin: 0px;
  }

  & > .ant-menu-item > a {
    padding: ${({theme:e})=>4*e.gridUnit}px;
  }
`,c=(0,r.iK)(a.Z.SubMenu)`
  color: ${({theme:e})=>e.colors.grayscale.dark1};
  border-bottom: none;
  &:after {
    content: '';
    position: absolute;
    bottom: -3px;
    left: 50%;
    width: 0;
    height: 3px;
    opacity: 0;
    transform: translateX(-50%);
    transition: all ${({theme:e})=>e.transitionTiming}s;
    background-color: ${({theme:e})=>e.colors.primary.base};
  }
  &:focus {
    border-bottom: none;
    background-color: transparent;
    @media (max-width: 767px) {
      background-color: ${({theme:e})=>e.colors.primary.light5};
    }
  }

  .ant-menu-submenu-open,
  .ant-menu-submenu-active {
    background-color: ${({theme:e})=>e.colors.primary.light5};
    .ant-menu-submenu-title {
      color: ${({theme:e})=>e.colors.grayscale.dark1};
      background-color: ${({theme:e})=>e.colors.primary.light5};
      border-bottom: none;
      margin: 0;
      &:after {
        opacity: 1;
        width: calc(100% - 1);
      }
    }
  }
  .ant-menu-submenu-title {
    &:after {
      content: '';
      position: absolute;
      bottom: -3px;
      left: 50%;
      width: 0;
      height: 3px;
      opacity: 0;
      transform: translateX(-50%);
      transition: all ${({theme:e})=>e.transitionTiming}s;
      background-color: ${({theme:e})=>e.colors.primary.base};
    }
  }
  & > .ant-menu-submenu-title {
    padding: 0 ${({theme:e})=>6*e.gridUnit}px 0
      ${({theme:e})=>3*e.gridUnit}px !important;
    span[role='img'] {
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
      margin-right: 0;
      svg {
        font-size: ${({theme:e})=>6*e.gridUnit}px;
        color: ${({theme:e})=>e.colors.grayscale.base};
      }
    }
    &:hover {
      color: ${({theme:e})=>e.colors.primary.base};
    }
  }
`,d=Object.assign(a.Z,{Item:s}),u=Object.assign(l,{Item:s,SubMenu:c,Divider:a.Z.Divider,ItemGroup:a.Z.ItemGroup}),_=(0,r.iK)(o.Z)`
  padding-top: ${({theme:e})=>(0,i.w)()||window.location.search.includes("?target_id=")?0:e.navMenuHeight}px; // 修改用研平台顶部空白问题
  box-sizing: border-box;
  overflow: hidden;
  .menuunbtn {
    position: absolute;
    bottom: 0;
    z-index: 10;
  }
  .menuunbtn .btnsvg {
    color: #b3c2d5;
  }
`},601304:(e,t,n)=>{n.d(t,{Z:()=>s});var r=n(667294),a=n(774069),o=n(835932),i=n(211965);const s=r.forwardRef(((e,t)=>{const[n,s]=(0,r.useState)(!1),{beforeOpen:l=(()=>{}),onExit:c=(()=>{}),isButton:d=!1,resizable:u=!1,draggable:_=!1,className:m="",tooltip:p,modalFooter:E,triggerNode:g,destroyOnClose:h=!0,modalBody:f,draggableConfig:A={},resizableConfig:T={},modalTitle:S,responsive:b,width:N,maxWidth:y}=e,v=()=>{s(!1),null==c||c()},I=e=>{e.preventDefault(),null==l||l(),s(!0)};return t&&(t.current={close:v,open:I}),(0,i.tZ)(r.Fragment,null,d&&(0,i.tZ)(o.Z,{className:"modal-trigger","data-test":"btn-modal-trigger",tooltip:p,onClick:I},g),!d&&(0,i.tZ)("span",{"data-test":"span-modal-trigger",onClick:I,role:"button"},g),(0,i.tZ)(a.Z,{className:m,show:n,onHide:v,title:S,footer:E,hideFooter:!E,width:N,maxWidth:y,responsive:b,resizable:u,resizableConfig:T,draggable:_,draggableConfig:A,destroyOnClose:h},f))}))},287183:(e,t,n)=>{n.d(t,{Y:()=>s});var r=n(751995),a=n(747933);const o=(0,r.iK)(a.ZP)`
  .ant-radio-inner {
    top: -1px;
    left: 2px;
    width: ${({theme:e})=>4*e.gridUnit}px;
    height: ${({theme:e})=>4*e.gridUnit}px;
    border-width: 2px;
    border-color: ${({theme:e})=>e.colors.grayscale.light2};
  }

  .ant-radio.ant-radio-checked {
    .ant-radio-inner {
      border-width: ${({theme:e})=>e.gridUnit+1}px;
      border-color: ${({theme:e})=>e.colors.primary.base};
    }

    .ant-radio-inner::after {
      background-color: ${({theme:e})=>e.colors.grayscale.light5};
      top: 0;
      left: 0;
      width: ${({theme:e})=>e.gridUnit+2}px;
      height: ${({theme:e})=>e.gridUnit+2}px;
    }
  }

  .ant-radio:hover,
  .ant-radio:focus {
    .ant-radio-inner {
      border-color: ${({theme:e})=>e.colors.primary.dark1};
    }
  }
`,i=(0,r.iK)(a.ZP.Group)`
  font-size: inherit;
`,s=Object.assign(o,{Group:i,Button:a.ZP.Button})},486057:(e,t,n)=>{n.d(t,{Z:()=>l});var r=n(211965),a=(n(667294),n(751995)),o=n(178186),i=n(731293),s=n(358593);const l=function({warningMarkdown:e,size:t}){const n=(0,a.Fg)();return(0,r.tZ)(s.u,{id:"warning-tooltip",title:(0,r.tZ)(o.Z,{source:e})},(0,r.tZ)(i.Z.AlertSolid,{iconColor:n.colors.alert.base,iconSize:t,css:(0,r.iv)({marginRight:2*n.gridUnit},"","")}))}},680621:(e,t,n)=>{n.d(t,{AA:()=>D,Bu:()=>V,C3:()=>p,D0:()=>l,Dp:()=>f,ES:()=>_,Ep:()=>q,HE:()=>P,Jd:()=>d,Kt:()=>B,LX:()=>b,M2:()=>o,Mu:()=>v,NN:()=>T,NT:()=>W,Nb:()=>u,Nz:()=>c,OE:()=>C,PV:()=>a,Pj:()=>w,Q9:()=>k,Qq:()=>N,TN:()=>G,VR:()=>H,Wf:()=>y,Xf:()=>h,Xk:()=>A,Z1:()=>m,Zn:()=>s,_4:()=>i,_B:()=>K,b5:()=>$,cd:()=>I,cx:()=>L,dU:()=>z,es:()=>R,fw:()=>x,gR:()=>S,kS:()=>F,pQ:()=>U,u_:()=>Z,ut:()=>M,vD:()=>E,x4:()=>g});var r=n(454076);const a="GRID_ID",o="HEADER_ID",i="ROOT_ID",s="DASHBOARD_VERSION_KEY",l="NEW_COMPONENTS_SOURCE_ID",c="NEW_STANDBY_COMPONENTS_SOURCE_ID",d="NEW_CHART_ID",u="NEW_COLUMN_ID",_="NEW_DIVIDER_ID",m="NEW_HEADER_ID",p="NEW_MARKDOWN_ID",E="NEW_ROW_ID",g="NEW_UPLOADS_ID",h="NEW_RECTBOX_ID",f=" NEW_ARROW_ID",A="NEW_TAB_ID",T="NEW_TABS_ID",S="NEW_DYNAMIC_COMPONENT",b="NEW_FILTERS_BTN_ID",N="NEW_FILTERS_SELECT_ID",y="NEW_WEB_COMPONENT_ID",v=4,I=8,R=16,O=(0,r.cz)(),L=1,D=5,x=O/2,w=8,Z="SMALL_HEADER",C="MEDIUM_HEADER",U="LARGE_HEADER",$="BACKGROUND_WHITE",P="BACKGROUND_TRANSPARENT",B="12",M="SimSun",H="#FFFFFF",k=50,G="overwrite",W="overwriteConfirmed",F="newDashboard",V=131071,q=["LABEL"],z="ALL_FILTERS_ROOT";var K;!function(e){e[e.NONE=0]="NONE",e[e.HIDE_NAV=1]="HIDE_NAV",e[e.HIDE_NAV_AND_TITLE=2]="HIDE_NAV_AND_TITLE",e[e.REPORT=3]="REPORT"}(K||(K={}))},269856:(e,t,n)=>{n.d(t,{Ak:()=>_,CO:()=>D,GE:()=>p,GS:()=>c,H7:()=>N,LT:()=>l,No:()=>L,Ps:()=>i,Q_:()=>h,Qi:()=>S,RB:()=>u,Wq:()=>y,YY:()=>o,Yd:()=>b,d:()=>s,ft:()=>A,i2:()=>T,iT:()=>x,kc:()=>v,m_:()=>f,qB:()=>E,qK:()=>m,u3:()=>O,vK:()=>I,xA:()=>R,xN:()=>Z,yi:()=>g,zu:()=>w});var r=n(455867),a=n(427600);const o={AVG:"AVG",COUNT:"COUNT",COUNT_DISTINCT:"COUNT_DISTINCT",MAX:"MAX",MIN:"MIN",SUM:"SUM"},i=Object.values(o);var s;!function(e){e.EQUALS="EQUALS",e.NOT_EQUALS="NOT_EQUALS",e.LESS_THAN="LESS_THAN",e.LESS_THAN_OR_EQUAL="LESS_THAN_OR_EQUAL",e.GREATER_THAN="GREATER_THAN",e.GREATER_THAN_OR_EQUAL="GREATER_THAN_OR_EQUAL",e.IN="IN",e.NOT_IN="NOT_IN",e.LIKE="LIKE",e.ILIKE="ILIKE",e.REGEX="REGEX",e.IS_NOT_NULL="IS_NOT_NULL",e.IS_NULL="IS_NULL",e.LATEST_PARTITION="LATEST_PARTITION",e.IS_TRUE="IS_TRUE",e.IS_FALSE="IS_FALSE",e.TEMPORAL_RANGE="TEMPORAL_RANGE"}(s||(s={}));const l={[s.EQUALS]:{display:(0,r.t)("Equal to (=)"),operation:"=="},[s.NOT_EQUALS]:{display:(0,r.t)("Not equal to (\u2260)"),operation:"!="},[s.LESS_THAN]:{display:(0,r.t)("Less than (<)"),operation:"<"},[s.LESS_THAN_OR_EQUAL]:{display:(0,r.t)("Less or equal (<=)"),operation:"<="},[s.GREATER_THAN]:{display:(0,r.t)("Greater than (>)"),operation:">"},[s.GREATER_THAN_OR_EQUAL]:{display:(0,r.t)("Greater or equal (>=)"),operation:">="},[s.IN]:{display:(0,r.t)("In"),operation:"IN"},[s.NOT_IN]:{display:(0,r.t)("Not in"),operation:"NOT IN"},[s.LIKE]:{display:(0,r.t)("Like"),operation:"LIKE"},[s.ILIKE]:{display:(0,r.t)("Like (case insensitive)"),operation:"ILIKE"},[s.REGEX]:{display:(0,r.t)("Regex"),operation:"REGEX"},[s.IS_NOT_NULL]:{display:(0,r.t)("Is not null"),operation:"IS NOT NULL"},[s.IS_NULL]:{display:(0,r.t)("Is null"),operation:"IS NULL"},[s.LATEST_PARTITION]:{display:(0,r.t)("use latest_partition template"),operation:"LATEST PARTITION"},[s.IS_TRUE]:{display:(0,r.t)("Is true"),operation:"=="},[s.IS_FALSE]:{display:(0,r.t)("Is false"),operation:"=="},[s.TEMPORAL_RANGE]:{display:(0,r.t)("TEMPORAL_RANGE"),operation:"TEMPORAL_RANGE"}},c=Object.values(s),d=[s.LATEST_PARTITION,s.IS_TRUE,s.IS_FALSE,s.TEMPORAL_RANGE],u=Object.keys(l).map((e=>{const t=l[e];return{label:t.display,value:e,operation:t.operation,operatorId:e}})).filter((e=>!d.includes(e.operatorId))),_=(s.LIKE,s.ILIKE,[s.EQUALS,s.NOT_EQUALS,s.LESS_THAN,s.LESS_THAN_OR_EQUAL,s.GREATER_THAN,s.GREATER_THAN_OR_EQUAL]),m=new Set([s.IN,s.NOT_IN,s.EQUALS,s.NOT_EQUALS]),p=new Set([s.IN,s.NOT_IN]),E=new Set([s.LATEST_PARTITION,s.TEMPORAL_RANGE]),g=[s.IS_NOT_NULL,s.IS_NULL,s.LATEST_PARTITION,s.IS_TRUE,s.IS_FALSE],h=/^(LONG|DOUBLE|FLOAT)?(SUM|AVG|MAX|MIN|COUNT)\([A-Z0-9_."]*\)$/i,f={time_range:(0,r.t)("Time range"),granularity_sqla:(0,r.t)("Time column"),time_grain_sqla:(0,r.t)("Time grain"),granularity:(0,r.t)("Time granularity")},A={CLEARABLE:"clearable",DEFAULT_VALUE:"defaultValue",MULTIPLE:"multiple",SEARCH_ALL_OPTIONS:"searchAllOptions",SORT_ASCENDING:"asc",SORT_METRIC:"metric"},T={time_range:"__time_range",granularity_sqla:"__time_col",time_grain_sqla:"__time_grain",granularity:"__granularity"};var S;!function(e){e.CONVERTED="CONVERTED",e.NOOP="NOOP",e.REVIEWING="REVIEWING",e.SNOOZED="SNOOZED",e.UNDECIDED="UNDECIDED"}(S||(S={}));const b=864e5,N=240,y=360,v=320,I=296,R=0,O=[{value:"1",label:"\u73af\u6bd4\u589e\u957f\u7387",key:"1",includes:a.Vg},{value:"2",label:"\u73af\u6bd4\u589e\u957f\u503c",key:"2",includes:a.Vg}],L=[{value:"6",label:"\u672c\u6708\u540c\u6bd4\u589e\u957f\u7387",key:"6",includes:["P1D"]},{value:"7",label:"\u672c\u6708\u540c\u6bd4\u6570\u636e\u503c",key:"7",includes:["P1D"]},{value:"9",label:"\u672c\u5e74\u540c\u6bd4\u589e\u957f\u7387",key:"9",includes:["P1D","P1M"]},{value:"10",label:"\u672c\u5e74\u540c\u6bd4\u589e\u957f\u503c",key:"10",includes:["P1D","P1M"]},{value:"13",label:"\u540c\u6bd4\u589e\u957f\u7387",key:"13",includes:["P3M","P1W"]},{value:"14",label:"\u540c\u6bd4\u589e\u957f\u503c",key:"14",includes:["P3M","P1W"]}],D=[{value:"ratio",label:"\u5360\u6bd4",key:"ratio"}],x=[{value:"yoy",label:"\u540c\u6bd4",key:"yoy"},{value:"qoq",label:"\u73af\u6bd4",key:"qoq"}],w=["1","6","9","13"],Z=["2","7","10","14"]},340219:(e,t,n)=>{n.d(t,{BR:()=>s,LW:()=>u,nv:()=>d});var r=n(957557),a=n.n(r),o=n(431069);const i=["url_params"],s=e=>a()(e,i),l=(e,t)=>{let n="api/v1/explore/form_data";return e&&(n=n.concat(`/${e}`)),t&&(n=n.concat(`?tab_id=${t}`)),n},c=(e,t,n,r)=>{const a={datasource_id:e,datasource_type:t,form_data:JSON.stringify(s(n))};return r&&(a.chart_id=r),a},d=(e,t,n,r,a)=>o.Z.post({endpoint:l(void 0,a),jsonPayload:c(e,t,n,r)}).then((e=>e.json.key)),u=(e,t,n,r,a,i)=>o.Z.put({endpoint:l(n,i),jsonPayload:c(e,t,r,a)}).then((e=>e.json.message))},242190:(e,t,n)=>{n.d(t,{l6:()=>s,ni:()=>r,s_:()=>c});var r,a=n(522102),o=n(667294);!function(e){e.LOADING="loading",e.COMPLETE="complete",e.ERROR="error"}(r||(r={}));const i={status:r.LOADING,result:null,error:null};function s(e,t){return(0,o.useMemo)((()=>{if(e.status!==r.COMPLETE)return e;try{return{...e,result:t(e.result)}}catch(e){return{status:r.ERROR,result:null,error:e}}}),[e,t])}const l=e=>e.result;function c(e){return s(function(e){const[t,n]=(0,o.useState)(i),s=(0,o.useRef)((()=>{}));return(0,o.useEffect)((()=>{n(i),s.current();let t=!1;return s.current=()=>{t=!0},(0,a.Z)({method:"GET",endpoint:e})({}).then((e=>{t||n({status:r.COMPLETE,result:e,error:null})})).catch((e=>{t||n({status:r.ERROR,result:null,error:e})})),()=>{t=!0}}),[e]),t}(e),l)}},741427:(e,t,n)=>{n.d(t,{D:()=>a});var r=n(667294);function a(e,t){const n=(0,r.useRef)(t);return(0,r.useEffect)((()=>{n.current=e}),[e]),n.current}},203741:(e,t,n)=>{n.d(t,{$b:()=>s,CQ:()=>I,Eh:()=>A,Ep:()=>d,Ev:()=>o,FY:()=>f,H3:()=>_,Iq:()=>l,Kr:()=>v,P$:()=>S,PC:()=>E,Ph:()=>h,Qg:()=>g,S:()=>m,Sr:()=>L,TA:()=>T,TD:()=>c,TY:()=>x,W9:()=>r,Wl:()=>i,Yd:()=>w,ZX:()=>D,aD:()=>a,kV:()=>b,n2:()=>y,oA:()=>O,oK:()=>p,vH:()=>u,xE:()=>R,yw:()=>N});const r="load_chart",a="render_chart",o="hide_browser_tab",i="mount_dashboard",s="mount_explorer",l="select_dashboard_tab",c="force_refresh_chart",d="change_explore_controls",u="toggle_edit_dashboard",_="force_refresh_dashboard",m="periodic_render_dashboard",p="explore_dashboard_chart",E="export_csv_dashboard_chart",g="change_dashboard_filter",h="dataset_creation_empty_cancellation",f="dataset_creation_database_cancellation",A="dataset_creation_schema_cancellation",T="dataset_creation_table_cancellation",S="dataset_creation_success",b="spa_navigation",N="confirm_overwrite_dashboard_metadata",y="dashboard_download_as_image",v="dashboard_download_as_pdf",I="dashboard_download_as_ppt",R="chart_download_as_image",O="chart_download_as_pdf",L="chart_download_as_ppt",D="sqllab_warn_local_storage_usage",x=new Set([r,a,o]),w=(new Set([i,l,p,c,E,g,d,u,_,m,s,N,y,R,O,"chart_download_as_excel",v,"dashboard_download_as_excel"]),{timeOriginOffset:0,markTimeOrigin(){this.timeOriginOffset=window.performance.now()},getTimestamp(){return Math.round(window.performance.now()-this.timeOriginOffset)}})},797381:(e,t,n)=>{n.r(t),n.d(t,{LOG_EVENT:()=>r,logEvent:()=>a});const r="LOG_EVENT";function a(e,t){return n=>n({type:r,payload:{eventName:e,eventData:t}})}},961337:(e,t,n)=>{var r;function a(e,t){try{const n=localStorage.getItem(e);return null===n?t:JSON.parse(n)}catch{return t}}function o(e,t){try{localStorage.setItem(e,JSON.stringify(t))}catch{}}function i(e,t){return a(e,t)}function s(e,t){o(e,t)}n.d(t,{I_:()=>o,LS:()=>s,OH:()=>a,dR:()=>r,rV:()=>i}),function(e){e.filter_box_transition_snoozed_at="filter_box_transition_snoozed_at",e.db="db",e.chart_split_sizes="chart_split_sizes",e.controls_width="controls_width",e.datasource_width="datasource_width",e.is_datapanel_open="is_datapanel_open",e.homepage_chart_filter="homepage_chart_filter",e.homepage_dashboard_filter="homepage_dashboard_filter",e.homepage_collapse_state="homepage_collapse_state",e.homepage_activity_filter="homepage_activity_filter",e.datasetname_set_successful="datasetname_set_successful",e.sqllab__is_autocomplete_enabled="sqllab__is_autocomplete_enabled",e.explore__data_table_original_formatted_time_columns="explore__data_table_original_formatted_time_columns",e.dashboard__custom_filter_bar_widths="dashboard__custom_filter_bar_widths",e.dashboard__explore_context="dashboard__explore_context",e.common__resizable_sidebar_widths="common__resizable_sidebar_widths"}(r||(r={}))},309679:(e,t,n)=>{n.d(t,{o:()=>o});var r=n(150361),a=n.n(r);function o(e,t){const n=new Set;return JSON.stringify(e,((e,t)=>{if("object"===typeof t&&null!==t){if(n.has(t))try{return a()(t)}catch(e){return}n.add(t)}return t}),t)}}}]);