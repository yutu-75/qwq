"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[18782],{418782:(e,t,n)=>{n.d(t,{p:()=>oe,Z:()=>ie});var l=n(205872),a=n.n(l),r=n(751995),i=n(455867),o=n(667294),s=n(229487),d=n(294184),c=n.n(d),p=n(835932),u=n(731293),g=n(94301),h=n(849576),m=n(64158),b=n(397754),f=n(211965);const v=r.iK.div`
  ${({theme:e,showThumbnails:t})=>`\n    display: grid;\n    grid-gap: ${12*e.gridUnit}px ${4*e.gridUnit}px;\n    grid-template-columns: repeat(auto-fit, 300px);\n    margin-top: ${-6*e.gridUnit}px;\n    padding: ${t?`${8*e.gridUnit+3}px ${9*e.gridUnit}px`:`${8*e.gridUnit+1}px ${9*e.gridUnit}px`};\n  `}
`,y=r.iK.div`
  border: 2px solid transparent;
  &.card-selected {
    border: 2px solid ${({theme:e})=>e.colors.primary.base};
  }
  &.bulk-select {
    cursor: pointer;
  }
`;function x({bulkSelectEnabled:e,loading:t,prepareRow:n,renderCard:l,rows:a,showThumbnails:r}){return l?(0,f.tZ)(v,{showThumbnails:r},t&&0===a.length&&[...new Array(25)].map(((e,n)=>(0,f.tZ)("div",{key:n},l({loading:t})))),a.length>0&&a.map((a=>l?(n(a),(0,f.tZ)(y,{className:c()({"card-selected":e&&a.isSelected,"bulk-select":e}),key:a.id,onClick:t=>{return n=t,l=a.toggleRowSelected,void(e&&(n.preventDefault(),n.stopPropagation(),l()));var n,l},role:"none"},l({...a.original,loading:t}))):null))):null}var w=n(468135),Z=n(49937),S=n(618446),k=n.n(S),C=n(379521),$=n(535755),I=n(115926),P=n.n(I);const _={encode:e=>void 0===e?void 0:P().encode(e).replace(/%/g,"%25").replace(/&/g,"%26").replace(/\+/g,"%2B").replace(/#/g,"%23"),decode:e=>void 0===e||Array.isArray(e)?void 0:P().decode(e)};class T extends Error{constructor(...e){super(...e),this.name="ListViewError"}}function N(e,t){return e.map((({id:e,urlDisplay:n,operator:l})=>({id:e,urlDisplay:n,operator:l,value:t[n||e]})))}function F(e,t){const n=[],l={};return Object.keys(e).forEach((t=>{const a={id:t,value:e[t]};l[t]=a,n.push(a)})),t.forEach((e=>{const t=e.urlDisplay||e.id,n=l[t];n&&(n.operator=e.operator,n.id=e.id)})),n}function R({fetchData:e,columns:t,data:n,count:l,initialPageSize:a,initialFilters:r=[],initialSort:i=[],bulkSelectMode:s=!1,bulkSelectColumnConfig:d,renderCard:c=!1,defaultViewMode:p="card"}){const[u,g]=(0,$.Kx)({filters:_,pageIndex:$.yz,sortColumn:$.Zp,sortOrder:$.Zp,viewMode:$.Zp,standalone:$.Zp,control:$.Zp});let h;u.control&&atob(u.control)&&(h=JSON.parse(atob(u.control)));const m=(0,o.useMemo)((()=>u.sortColumn&&u.sortOrder?[{id:u.sortColumn,desc:"desc"===u.sortOrder}]:i),[u.sortColumn,u.sortOrder]),b={filters:u.filters?F(u.filters,r):[],pageIndex:u.pageIndex||0,pageSize:a,sortBy:m},[f,v]=(0,o.useState)(u.viewMode||(c?p:"table")),y=(0,o.useMemo)((()=>{const e=t.map((e=>({...e,filter:"exact"})));return s?[d,...e]:e}),[s,t]),{getTableProps:x,getTableBodyProps:w,headerGroups:Z,rows:S,prepareRow:I,canPreviousPage:P,canNextPage:T,pageCount:R,gotoPage:A,setAllFilters:U,selectedFlatRows:B,toggleAllRowsSelected:E,state:{pageIndex:z,pageSize:M,sortBy:V,filters:K}}=(0,C.useTable)({columns:y,count:l,data:n,disableFilters:!0,disableSortRemove:!0,initialState:b,manualFilters:!0,manualPagination:!0,manualSortBy:!0,autoResetFilters:!1,pageCount:Math.ceil(l/a)},C.useFilters,C.useSortBy,C.usePagination,C.useRowState,C.useRowSelect),[D,H]=(0,o.useState)(u.filters&&r.length?N(r,u.filters):[]);(0,o.useEffect)((()=>{r.length&&H(N(r,u.filters?u.filters:{}))}),[r]),(0,o.useEffect)((()=>{const t={};D.forEach((e=>{if(void 0!==e.value&&("string"!==typeof e.value||e.value.length>0)){const n=e.urlDisplay||e.id;t[n]=e.value}}));const n={filters:Object.keys(t).length?t:void 0,pageIndex:z,standalone:u.standalone};null!==h&&(n.control=u.control),V[0]&&(n.sortColumn=V[0].id,n.sortOrder=V[0].desc?"desc":"asc"),c&&(n.viewMode=f);const l="undefined"!==typeof u.pageIndex&&n.pageIndex!==u.pageIndex?"push":"replace";g(n,l),e({pageIndex:z,pageSize:M,sortBy:V,filters:K})}),[e,z,M,V,K]),(0,o.useEffect)((()=>{k()(b.pageIndex,z)||A(b.pageIndex)}),[u]);return{canNextPage:T,canPreviousPage:P,getTableBodyProps:w,getTableProps:x,gotoPage:A,headerGroups:Z,pageCount:R,prepareRow:I,rows:S,selectedFlatRows:B,setAllFilters:U,state:{pageIndex:z,pageSize:M,sortBy:V,filters:K,internalFilters:D,viewMode:f,control:h},toggleAllRowsSelected:E,applyFilterValue:(e,t)=>{H((n=>{if(n[e].value===t)return n;const l={...n[e],value:t},a=function(e,t,n){const l=e.find(((e,n)=>t===n));return[...e.slice(0,t),{...l,...n},...e.slice(t+1)]}(n,e,l);return U(a.filter((e=>!("undefined"===typeof e.value||Array.isArray(e.value)&&!e.value.length))).map((({value:e,operator:t,id:n})=>"between"===t&&Array.isArray(e)?[{value:e[0],operator:"gt",id:n},{value:e[1],operator:"lt",id:n}]:{value:e,operator:t,id:n})).flat()),A(0),a}))},setViewMode:v,query:u}}var A=n(49238);const U=r.iK.div`
  width: ${200}px;
`,B=(0,r.iK)(u.Z.Search)`
  color: ${({theme:e})=>e.colors.grayscale.light1};
`,E=(0,r.iK)(Z.oc)`
  border-radius: ${({theme:e})=>e.gridUnit}px;
`;function z({Header:e,name:t,initialValue:n,onSubmit:l},a){const[r,s]=(0,o.useState)(n||""),d=()=>{r&&l(r.trim())};return(0,o.useImperativeHandle)(a,(()=>({clearFilter:()=>{s(""),l("")}}))),(0,f.tZ)(U,null,(0,f.tZ)(A.lX,null,e),(0,f.tZ)(E,{allowClear:!0,"data-test":"filters-search",placeholder:(0,i.t)("Type a value"),name:t,value:r,onChange:e=>{s(e.currentTarget.value),""===e.currentTarget.value&&l("")},onPressEnter:d,onBlur:d,prefix:(0,f.tZ)(B,{iconSize:"l"})}))}const M=(0,o.forwardRef)(z);var V=n(784101);const K=r.iK.div`
  display: inline-flex;
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
  align-items: center;
  width: ${200}px;
`;function D({Header:e,name:t,fetchSelects:n,initialValue:l,onSelect:a,selects:r=[]},s){const[d,c]=(0,o.useState)(l),p=e=>{a(e?{label:e.label,value:e.value}:void 0),c(e)},u=()=>{a(void 0,!0),c(void 0)};(0,o.useImperativeHandle)(s,(()=>({clearFilter:()=>{u()}})));const g=(0,o.useMemo)((()=>async(e,t,l)=>{if(n){const a=await n(e,t,l);return{data:a.data,totalCount:a.totalCount}}return{data:[],totalCount:0}}),[n]);return(0,f.tZ)(K,null,n?(0,f.tZ)(V.Z,{allowClear:!0,ariaLabel:"string"===typeof e?e:t||(0,i.t)("Filter"),"data-test":"filters-select",header:(0,f.tZ)(A.lX,null,e),onChange:p,onClear:u,options:g,placeholder:(0,i.t)("Select or type a value"),showSearch:!0,value:d}):(0,f.tZ)(Z.Ph,{allowClear:!0,ariaLabel:"string"===typeof e?e:t||(0,i.t)("Filter"),"data-test":"filters-select",header:(0,f.tZ)(A.lX,null,e),labelInValue:!0,onChange:p,onClear:u,options:r,placeholder:(0,i.t)("Select or type a value"),showSearch:!0,value:d}))}const H=(0,o.forwardRef)(D);var O=n(730381),L=n.n(O),G=n(662276);const X=r.iK.div`
  display: inline-flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  width: 360px;
`;function q({Header:e,initialValue:t,onSubmit:n},l){const[a,r]=(0,o.useState)(null!=t?t:null),s=(0,o.useMemo)((()=>!a||Array.isArray(a)&&!a.length?null:[L()(a[0]),L()(a[1])]),[a]);return(0,o.useImperativeHandle)(l,(()=>({clearFilter:()=>{r(null),n([])}}))),(0,f.tZ)(X,null,(0,f.tZ)(A.lX,null,e),(0,f.tZ)(G.S,{placeholder:[(0,i.t)("Start date"),(0,i.t)("End date")],showTime:!0,value:s,onChange:e=>{var t,l,a,i;if(!e)return r(null),void n([]);const o=[null!=(t=null==(l=e[0])?void 0:l.valueOf())?t:0,null!=(a=null==(i=e[1])?void 0:i.valueOf())?a:0];r(o),n(o)}}))}const W=(0,o.forwardRef)(q);function j({filters:e,internalFilters:t=[],updateFilterValue:n},l){const a=(0,o.useMemo)((()=>Array.from({length:e.length},(()=>(0,o.createRef)()))),[e.length]);return(0,o.useImperativeHandle)(l,(()=>({clearFilters:()=>{a.forEach((e=>{var t;null==(t=e.current)||null==t.clearFilter||t.clearFilter()}))}}))),(0,f.tZ)(o.Fragment,null,e.map((({Header:e,fetchSelects:l,key:r,id:i,input:o,paginate:s,selects:d,onFilterUpdate:c},p)=>{var u;const g=null==t||null==(u=t[p])?void 0:u.value;return"select"===o?(0,f.tZ)(H,{ref:a[p],Header:e,fetchSelects:l,initialValue:g,key:r,name:i,onSelect:(e,t)=>{var l,i;"database"===r&&(a[p+1]&&(null==(l=a[p+1])||null==(i=l.current)||i.clearFilter()));c&&(t||c(e)),n(p,e)},paginate:s,selects:d}):"search"===o&&"string"===typeof e?(0,f.tZ)(M,{ref:a[p],Header:e,initialValue:g,key:r,name:i,onSubmit:e=>{c&&c(e),n(p,e)}}):"datetime_range"===o?(0,f.tZ)(W,{ref:a[p],Header:e,initialValue:g,key:r,name:i,onSubmit:e=>n(p,e)}):null})))}const J=(0,w.b)((0,o.forwardRef)(j)),Y=r.iK.div`
  display: inline-flex;
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
  align-items: center;
  text-align: left;
  width: ${200}px;
`,Q=({initialSort:e,onChange:t,options:n,pageIndex:l,pageSize:a})=>{const r=e&&n.find((({id:t})=>t===e[0].id))||n[0],[s,d]=(0,o.useState)({label:r.label,value:r.value}),c=(0,o.useMemo)((()=>n.map((e=>({label:e.label,value:e.value})))),[n]);return(0,f.tZ)(Y,null,(0,f.tZ)(Z.Ph,{ariaLabel:(0,i.t)("Sort"),header:(0,f.tZ)(A.lX,null,(0,i.t)("Sort")),labelInValue:!0,onChange:e=>(e=>{d(e);const r=n.find((({value:t})=>t===e.value));if(r){const e=[{id:r.id,desc:r.desc}];t({pageIndex:l,pageSize:a,sortBy:e,filters:[]})}})(e),options:c,showSearch:!0,value:s}))},ee=r.iK.div`
  text-align: center;

  .superset-list-view {
    text-align: left;
    border-radius: 4px 0;
    margin: 0 ${({theme:e})=>4*e.gridUnit}px;

    .header {
      display: flex;
      padding-bottom: ${({theme:e})=>4*e.gridUnit}px;

      & .controls {
        display: flex;
        flex-wrap: wrap;
        column-gap: ${({theme:e})=>6*e.gridUnit}px;
        row-gap: ${({theme:e})=>4*e.gridUnit}px;
      }
    }

    .body.empty table {
      margin-bottom: 0;
    }

    .body {
      overflow-x: auto;
    }

    .ant-empty {
      .ant-empty-image {
        height: auto;
      }
    }
  }

  .pagination-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-bottom: ${({theme:e})=>4*e.gridUnit}px;
  }

  .row-count-container {
    margin-top: ${({theme:e})=>2*e.gridUnit}px;
    color: ${({theme:e})=>e.colors.grayscale.base};
  }
`,te=(0,r.iK)(s.Z)`
  ${({theme:e})=>`\n    border-radius: 0;\n    margin-bottom: 0;\n    color: ${e.colors.grayscale.dark1};\n    background-color: ${e.colors.primary.light4};\n\n    .selectedCopy {\n      display: inline-block;\n      padding: ${2*e.gridUnit}px 0;\n    }\n\n    .deselect-all {\n      color: ${e.colors.primary.base};\n      margin-left: ${4*e.gridUnit}px;\n    }\n\n    .divider {\n      margin: ${2*-e.gridUnit}px 0 ${2*-e.gridUnit}px ${4*e.gridUnit}px;\n      width: 1px;\n      height: ${8*e.gridUnit}px;\n      box-shadow: inset -1px 0px 0px ${e.colors.grayscale.light2};\n      display: inline-flex;\n      vertical-align: middle;\n      position: relative;\n    }\n\n    .ant-alert-close-icon {\n      margin-top: ${1.5*e.gridUnit}px;\n    }\n  `}
`,ne={Cell:({row:e})=>(0,f.tZ)(h.Z,a()({},e.getToggleRowSelectedProps(),{id:e.id})),Header:({getToggleAllRowsSelectedProps:e})=>(0,f.tZ)(h.Z,a()({},e(),{id:"header-toggle-all"})),id:"selection",size:"sm"},le=r.iK.div`
  padding-right: ${({theme:e})=>4*e.gridUnit}px;
  margin-top: ${({theme:e})=>5*e.gridUnit+1}px;
  white-space: nowrap;
  display: inline-block;

  .toggle-button {
    display: inline-block;
    border-radius: ${({theme:e})=>e.gridUnit/2}px;
    padding: ${({theme:e})=>e.gridUnit}px;
    padding-bottom: ${({theme:e})=>.5*e.gridUnit}px;

    &:first-of-type {
      margin-right: ${({theme:e})=>2*e.gridUnit}px;
    }
  }

  .active {
    background-color: ${({theme:e})=>e.colors.grayscale.base};
    svg {
      color: ${({theme:e})=>e.colors.grayscale.light5};
    }
  }
`,ae=r.iK.div`
  padding: ${({theme:e})=>40*e.gridUnit}px 0;

  &.table {
    background: ${({theme:e})=>e.colors.grayscale.light5};
  }
`,re=({mode:e,setMode:t})=>(0,f.tZ)(le,null,(0,f.tZ)("div",{role:"button",tabIndex:0,onClick:e=>{e.currentTarget.blur(),t("card")},className:c()("toggle-button",{active:"card"===e})},(0,f.tZ)(u.Z.CardView,null)),(0,f.tZ)("div",{role:"button",tabIndex:0,onClick:e=>{e.currentTarget.blur(),t("table")},className:c()("toggle-button",{active:"table"===e})},(0,f.tZ)(u.Z.ListView,null)));const ie=function({columns:e,data:t,count:n,pageSize:l,fetchData:r,loading:s,initialSort:d=[],className:c="",filters:u=[],bulkActions:h=[],bulkSelectEnabled:v=!1,disableBulkSelect:y=(()=>{}),renderBulkSelectCopy:w=(e=>(0,i.t)("%s Selected",e.length)),renderCard:Z,showThumbnails:S,cardSortSelectOptions:k,defaultViewMode:C="card",highlightRowId:$,emptyState:I}){const{getTableProps:P,getTableBodyProps:_,headerGroups:N,rows:F,prepareRow:A,pageCount:U=1,gotoPage:B,applyFilterValue:E,selectedFlatRows:z,toggleAllRowsSelected:M,setViewMode:V,state:{pageIndex:K,pageSize:D,internalFilters:H,viewMode:O},query:L}=R({bulkSelectColumnConfig:ne,bulkSelectMode:v&&Boolean(h.length),columns:e,count:n,data:t,fetchData:r,initialPageSize:l,initialSort:d,initialFilters:u,renderCard:Boolean(Z),defaultViewMode:C}),G=Boolean(u.length);if(G){const t=e.reduce(((e,t)=>({...e,[t.id||t.accessor]:!0})),{});u.forEach((e=>{if(!t[e.id])throw new T(`Invalid filter config, ${e.id} is not present in columns`)}))}const X=(0,o.useRef)(null),q=(0,o.useCallback)((()=>{var e;L.filters&&(null==(e=X.current)||e.clearFilters())}),[L.filters]),W=Boolean(Z);return(0,o.useEffect)((()=>{v||M(!1)}),[v,M]),(0,f.tZ)(ee,null,(0,f.tZ)("div",{"data-test":c,className:`superset-list-view ${c}`},(0,f.tZ)("div",{className:"header"},W&&(0,f.tZ)(re,{mode:O,setMode:V}),(0,f.tZ)("div",{className:"controls"},G&&(0,f.tZ)(J,{ref:X,filters:u,internalFilters:H,updateFilterValue:E}),"card"===O&&k&&(0,f.tZ)(Q,{initialSort:d,onChange:r,options:k,pageIndex:K,pageSize:D}))),(0,f.tZ)("div",{className:"body "+(0===F.length?"empty":"")},v&&(0,f.tZ)(te,{"data-test":"bulk-select-controls",type:"info",closable:!0,showIcon:!1,onClose:y,message:(0,f.tZ)(o.Fragment,null,(0,f.tZ)("div",{className:"selectedCopy","data-test":"bulk-select-copy"},w(z)),Boolean(z.length)&&(0,f.tZ)(o.Fragment,null,(0,f.tZ)("span",{"data-test":"bulk-select-deselect-all",role:"button",tabIndex:0,className:"deselect-all",onClick:()=>M(!1)},(0,i.t)("Deselect all")),(0,f.tZ)("div",{className:"divider"}),h.map((e=>(0,f.tZ)(p.Z,{"data-test":"bulk-select-action",key:e.key,buttonStyle:e.type,cta:!0,onClick:()=>e.onSelect(z.map((e=>e.original)))},e.name)))))}),"card"===O&&(0,f.tZ)(x,{bulkSelectEnabled:v,prepareRow:A,renderCard:Z,rows:F,loading:s,showThumbnails:S}),"table"===O&&(0,f.tZ)(b.Z,{getTableProps:P,getTableBodyProps:_,prepareRow:A,headerGroups:N,rows:F,columns:e,loading:s,highlightRowId:$}),!s&&0===F.length&&(0,f.tZ)(ae,{className:O},L.filters?(0,f.tZ)(g.XJ,{title:(0,i.t)("No results match your filter criteria"),description:(0,i.t)("Try different criteria to display results."),image:"filter-results.svg",buttonAction:()=>q(),buttonText:(0,i.t)("clear all filters")}):(0,f.tZ)(g.XJ,a()({},I,{title:(null==I?void 0:I.title)||(0,i.t)("No Data"),image:(null==I?void 0:I.image)||"filter-results.svg"}))))),F.length>0&&(0,f.tZ)("div",{className:"pagination-container"},(0,f.tZ)(m.Z,{totalPages:U||0,currentPage:U?K+1:0,onChange:e=>B(e-1),hideFirstAndLastPageLinks:!0}),(0,f.tZ)("div",{className:"row-count-container"},!s&&(0,i.t)("%s-%s of %s",D*K+(F.length&&1),D*K+F.length,n))))};var oe;!function(e){e.startsWith="sw",e.endsWith="ew",e.contains="ct",e.equals="eq",e.notStartsWith="nsw",e.notEndsWith="new",e.notContains="nct",e.notEquals="neq",e.greaterThan="gt",e.lessThan="lt",e.relationManyMany="rel_m_m",e.relationOneMany="rel_o_m",e.titleOrSlug="title_or_slug",e.nameOrDescription="name_or_description",e.allText="all_text",e.chartAllText="chart_all_text",e.datasetIsNullOrEmpty="dataset_is_null_or_empty",e.between="between",e.dashboardIsFav="dashboard_is_favorite",e.chartIsFav="chart_is_favorite",e.chartIsCertified="chart_is_certified",e.dashboardIsCertified="dashboard_is_certified",e.datasetIsCertified="dataset_is_certified",e.dashboardHasCreatedBy="dashboard_has_created_by",e.chartHasCreatedBy="chart_has_created_by"}(oe||(oe={}))},64158:(e,t,n)=>{n.d(t,{Z:()=>p});n(667294);var l=n(751995),a=n(294184),r=n.n(a),i=n(211965);const o=l.iK.ul`
  display: inline-block;
  margin: 16px 0;
  padding: 0;

  li {
    display: inline;
    margin: 0 4px;

    span {
      padding: 8px 12px;
      text-decoration: none;
      background-color: ${({theme:e})=>e.colors.grayscale.light5};
      border-radius: ${({theme:e})=>e.borderRadius}px;

      &:hover,
      &:focus {
        z-index: 2;
        color: ${({theme:e})=>e.colors.grayscale.dark1};
        background-color: ${({theme:e})=>e.colors.grayscale.light3};
      }
    }

    &.disabled {
      span {
        background-color: transparent;
        cursor: default;

        &:focus {
          outline: none;
        }
      }
    }
    &.active {
      span {
        z-index: 3;
        color: ${({theme:e})=>e.colors.grayscale.light5};
        cursor: default;
        background-color: ${({theme:e})=>e.colors.primary.base};

        &:focus {
          outline: none;
        }
      }
    }
  }
`;function s({children:e}){return(0,i.tZ)(o,{role:"navigation"},e)}s.Next=function({disabled:e,onClick:t}){return(0,i.tZ)("li",{className:r()({disabled:e})},(0,i.tZ)("span",{role:"button",tabIndex:e?-1:0,onClick:n=>{n.preventDefault(),e||t(n)}},"\xbb"))},s.Prev=function({disabled:e,onClick:t}){return(0,i.tZ)("li",{className:r()({disabled:e})},(0,i.tZ)("span",{role:"button",tabIndex:e?-1:0,onClick:n=>{n.preventDefault(),e||t(n)}},"\xab"))},s.Item=function({active:e,children:t,onClick:n}){return(0,i.tZ)("li",{className:r()({active:e})},(0,i.tZ)("span",{role:"button",tabIndex:e?-1:0,onClick:t=>{t.preventDefault(),e||n(t)}},t))},s.Ellipsis=function({disabled:e,onClick:t}){return(0,i.tZ)("li",{className:r()({disabled:e})},(0,i.tZ)("span",{role:"button",tabIndex:e?-1:0,onClick:n=>{n.preventDefault(),e||t(n)}},"\u2026"))};const d=s;var c=n(452630);const p=(0,c.YM)({WrapperComponent:d,itemTypeToComponent:{[c.iB.PAGE]:({value:e,isActive:t,onClick:n})=>(0,i.tZ)(d.Item,{active:t,onClick:n},e),[c.iB.ELLIPSIS]:({isActive:e,onClick:t})=>(0,i.tZ)(d.Ellipsis,{disabled:e,onClick:t}),[c.iB.PREVIOUS_PAGE_LINK]:({isActive:e,onClick:t})=>(0,i.tZ)(d.Prev,{disabled:e,onClick:t}),[c.iB.NEXT_PAGE_LINK]:({isActive:e,onClick:t})=>(0,i.tZ)(d.Next,{disabled:e,onClick:t}),[c.iB.FIRST_PAGE_LINK]:()=>null,[c.iB.LAST_PAGE_LINK]:()=>null}})},397754:(e,t,n)=>{n.d(t,{Z:()=>u});var l=n(205872),a=n.n(l),r=n(667294),i=n(294184),o=n.n(i),s=n(751995),d=n(731293),c=n(211965);const p=s.iK.table`
  ${({theme:e})=>`\n    background-color: ${e.colors.grayscale.light5};\n    border-collapse: separate;\n    border-radius: ${e.borderRadius}px;\n\n    thead > tr > th {\n      border: 0;\n    }\n\n    tbody {\n      tr:first-of-type > td {\n        border-top: 0;\n      }\n    }\n    th {\n      background: ${e.colors.grayscale.light5};\n      position: sticky;\n      top: 0;\n\n      &:first-of-type {\n        padding-left: ${4*e.gridUnit}px;\n      }\n\n      &.xs {\n        min-width: 25px;\n      }\n      &.sm {\n        min-width: 50px;\n      }\n      &.md {\n        min-width: 75px;\n      }\n      &.lg {\n        min-width: 100px;\n      }\n      &.xl {\n        min-width: 150px;\n      }\n      &.xxl {\n        min-width: 200px;\n      }\n\n      span {\n        white-space: nowrap;\n        display: flex;\n        align-items: center;\n        line-height: 2;\n      }\n\n      svg {\n        display: inline-block;\n        position: relative;\n      }\n    }\n\n    td {\n      &.xs {\n        width: 25px;\n      }\n      &.sm {\n        width: 50px;\n      }\n      &.md {\n        width: 75px;\n      }\n      &.lg {\n        width: 100px;\n      }\n      &.xl {\n        width: 150px;\n      }\n      &.xxl {\n        width: 200px;\n      }\n    }\n\n    .table-cell-loader {\n      position: relative;\n\n      .loading-bar {\n        background-color: ${e.colors.secondary.light4};\n        border-radius: 7px;\n\n        span {\n          visibility: hidden;\n        }\n      }\n\n      .empty-loading-bar {\n        display: inline-block;\n        width: 100%;\n        height: 1.2em;\n      }\n    }\n\n    .actions {\n      white-space: nowrap;\n      min-width: 100px;\n\n      svg,\n      i {\n        margin-right: 8px;\n\n        &:hover {\n          path {\n            fill: ${e.colors.primary.base};\n          }\n        }\n      }\n    }\n\n    .table-row {\n      .actions {\n        opacity: 0;\n        font-size: ${e.typography.sizes.xl}px;\n        display: flex;\n      }\n\n      &:hover {\n        background-color: ${e.colors.secondary.light5};\n\n        .actions {\n          opacity: 1;\n          transition: opacity ease-in ${e.transitionTiming}s;\n        }\n      }\n    }\n\n    .table-row-selected {\n      background-color: ${e.colors.secondary.light4};\n\n      &:hover {\n        background-color: ${e.colors.secondary.light4};\n      }\n    }\n\n    .table-cell {\n      font-feature-settings: 'tnum' 1;\n      text-overflow: ellipsis;\n      overflow: hidden;\n      max-width: 320px;\n      line-height: 1;\n      vertical-align: middle;\n      &:first-of-type {\n        padding-left: ${4*e.gridUnit}px;\n      }\n      &__wrap {\n        white-space: normal;\n      }\n      &__nowrap {\n        white-space: nowrap;\n      }\n    }\n\n    @keyframes loading-shimmer {\n      40% {\n        background-position: 100% 0;\n      }\n\n      100% {\n        background-position: 100% 0;\n      }\n    }\n  `}
`;p.displayName="table";const u=r.memo((({getTableProps:e,getTableBodyProps:t,prepareRow:n,headerGroups:l,columns:r,rows:i,loading:s,highlightRowId:u,columnsForWrapText:g})=>(0,c.tZ)(p,a()({},e(),{className:"table table-hover","data-test":"listview-table"}),(0,c.tZ)("thead",null,l.map((e=>(0,c.tZ)("tr",e.getHeaderGroupProps(),e.headers.map((e=>{let t=(0,c.tZ)(d.Z.Sort,null);return e.isSorted&&e.isSortedDesc?t=(0,c.tZ)(d.Z.SortDesc,null):e.isSorted&&!e.isSortedDesc&&(t=(0,c.tZ)(d.Z.SortAsc,null)),e.hidden?null:(0,c.tZ)("th",a()({},e.getHeaderProps(e.canSort?e.getSortByToggleProps():{}),{"data-test":"sort-header",className:o()({[e.size||""]:e.size})}),(0,c.tZ)("span",null,e.render("Header"),e.canSort&&t))})))))),(0,c.tZ)("tbody",t(),s&&0===i.length&&[...new Array(12)].map(((e,t)=>(0,c.tZ)("tr",{key:t},r.map(((e,t)=>e.hidden?null:(0,c.tZ)("td",{key:t,className:o()("table-cell",{"table-cell-loader":s})},(0,c.tZ)("span",{className:"loading-bar empty-loading-bar",role:"progressbar","aria-label":"loading"}))))))),i.length>0&&i.map((e=>{n(e);const t=e.original.id;return(0,c.tZ)("tr",a()({"data-test":"table-row"},e.getRowProps(),{className:o()("table-row",{"table-row-selected":e.isSelected||"undefined"!==typeof t&&t===u})}),e.cells.map((e=>{if(e.column.hidden)return null;const t=e.column.cellProps||{},n=null==g?void 0:g.includes(e.column.Header);return(0,c.tZ)("td",a()({"data-test":"table-row-cell",className:o()("table-cell table-cell__"+(n?"wrap":"nowrap"),{"table-cell-loader":s,[e.column.size||""]:e.column.size})},e.getCellProps(),t),(0,c.tZ)("span",{className:o()({"loading-bar":s}),role:s?"progressbar":void 0},(0,c.tZ)("span",{"data-test":"cell-text"},e.render("Cell"))))})))}))))))}}]);