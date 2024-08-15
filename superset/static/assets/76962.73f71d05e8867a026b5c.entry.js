"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[76962],{64158:(n,e,t)=>{t.d(e,{Z:()=>p});t(667294);var a=t(751995),l=t(294184),o=t.n(l),i=t(211965);const r=a.iK.ul`
  display: inline-block;
  margin: 16px 0;
  padding: 0;

  li {
    display: inline;
    margin: 0 4px;

    span {
      padding: 8px 12px;
      text-decoration: none;
      background-color: ${({theme:n})=>n.colors.grayscale.light5};
      border-radius: ${({theme:n})=>n.borderRadius}px;

      &:hover,
      &:focus {
        z-index: 2;
        color: ${({theme:n})=>n.colors.grayscale.dark1};
        background-color: ${({theme:n})=>n.colors.grayscale.light3};
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
        color: ${({theme:n})=>n.colors.grayscale.light5};
        cursor: default;
        background-color: ${({theme:n})=>n.colors.primary.base};

        &:focus {
          outline: none;
        }
      }
    }
  }
`;function s({children:n}){return(0,i.tZ)(r,{role:"navigation"},n)}s.Next=function({disabled:n,onClick:e}){return(0,i.tZ)("li",{className:o()({disabled:n})},(0,i.tZ)("span",{role:"button",tabIndex:n?-1:0,onClick:t=>{t.preventDefault(),n||e(t)}},"\xbb"))},s.Prev=function({disabled:n,onClick:e}){return(0,i.tZ)("li",{className:o()({disabled:n})},(0,i.tZ)("span",{role:"button",tabIndex:n?-1:0,onClick:t=>{t.preventDefault(),n||e(t)}},"\xab"))},s.Item=function({active:n,children:e,onClick:t}){return(0,i.tZ)("li",{className:o()({active:n})},(0,i.tZ)("span",{role:"button",tabIndex:n?-1:0,onClick:e=>{e.preventDefault(),n||t(e)}},e))},s.Ellipsis=function({disabled:n,onClick:e}){return(0,i.tZ)("li",{className:o()({disabled:n})},(0,i.tZ)("span",{role:"button",tabIndex:n?-1:0,onClick:t=>{t.preventDefault(),n||e(t)}},"\u2026"))};const d=s;var c=t(452630);const p=(0,c.YM)({WrapperComponent:d,itemTypeToComponent:{[c.iB.PAGE]:({value:n,isActive:e,onClick:t})=>(0,i.tZ)(d.Item,{active:e,onClick:t},n),[c.iB.ELLIPSIS]:({isActive:n,onClick:e})=>(0,i.tZ)(d.Ellipsis,{disabled:n,onClick:e}),[c.iB.PREVIOUS_PAGE_LINK]:({isActive:n,onClick:e})=>(0,i.tZ)(d.Prev,{disabled:n,onClick:e}),[c.iB.NEXT_PAGE_LINK]:({isActive:n,onClick:e})=>(0,i.tZ)(d.Next,{disabled:n,onClick:e}),[c.iB.FIRST_PAGE_LINK]:()=>null,[c.iB.LAST_PAGE_LINK]:()=>null}})},397754:(n,e,t)=>{t.d(e,{Z:()=>g});var a=t(205872),l=t.n(a),o=t(667294),i=t(294184),r=t.n(i),s=t(751995),d=t(731293),c=t(211965);const p=s.iK.table`
  ${({theme:n})=>`\n    background-color: ${n.colors.grayscale.light5};\n    border-collapse: separate;\n    border-radius: ${n.borderRadius}px;\n\n    thead > tr > th {\n      border: 0;\n    }\n\n    tbody {\n      tr:first-of-type > td {\n        border-top: 0;\n      }\n    }\n    th {\n      background: ${n.colors.grayscale.light5};\n      position: sticky;\n      top: 0;\n\n      &:first-of-type {\n        padding-left: ${4*n.gridUnit}px;\n      }\n\n      &.xs {\n        min-width: 25px;\n      }\n      &.sm {\n        min-width: 50px;\n      }\n      &.md {\n        min-width: 75px;\n      }\n      &.lg {\n        min-width: 100px;\n      }\n      &.xl {\n        min-width: 150px;\n      }\n      &.xxl {\n        min-width: 200px;\n      }\n\n      span {\n        white-space: nowrap;\n        display: flex;\n        align-items: center;\n        line-height: 2;\n      }\n\n      svg {\n        display: inline-block;\n        position: relative;\n      }\n    }\n\n    td {\n      &.xs {\n        width: 25px;\n      }\n      &.sm {\n        width: 50px;\n      }\n      &.md {\n        width: 75px;\n      }\n      &.lg {\n        width: 100px;\n      }\n      &.xl {\n        width: 150px;\n      }\n      &.xxl {\n        width: 200px;\n      }\n    }\n\n    .table-cell-loader {\n      position: relative;\n\n      .loading-bar {\n        background-color: ${n.colors.secondary.light4};\n        border-radius: 7px;\n\n        span {\n          visibility: hidden;\n        }\n      }\n\n      .empty-loading-bar {\n        display: inline-block;\n        width: 100%;\n        height: 1.2em;\n      }\n    }\n\n    .actions {\n      white-space: nowrap;\n      min-width: 100px;\n\n      svg,\n      i {\n        margin-right: 8px;\n\n        &:hover {\n          path {\n            fill: ${n.colors.primary.base};\n          }\n        }\n      }\n    }\n\n    .table-row {\n      .actions {\n        opacity: 0;\n        font-size: ${n.typography.sizes.xl}px;\n        display: flex;\n      }\n\n      &:hover {\n        background-color: ${n.colors.secondary.light5};\n\n        .actions {\n          opacity: 1;\n          transition: opacity ease-in ${n.transitionTiming}s;\n        }\n      }\n    }\n\n    .table-row-selected {\n      background-color: ${n.colors.secondary.light4};\n\n      &:hover {\n        background-color: ${n.colors.secondary.light4};\n      }\n    }\n\n    .table-cell {\n      font-feature-settings: 'tnum' 1;\n      text-overflow: ellipsis;\n      overflow: hidden;\n      max-width: 320px;\n      line-height: 1;\n      vertical-align: middle;\n      &:first-of-type {\n        padding-left: ${4*n.gridUnit}px;\n      }\n      &__wrap {\n        white-space: normal;\n      }\n      &__nowrap {\n        white-space: nowrap;\n      }\n    }\n\n    @keyframes loading-shimmer {\n      40% {\n        background-position: 100% 0;\n      }\n\n      100% {\n        background-position: 100% 0;\n      }\n    }\n  `}
`;p.displayName="table";const g=o.memo((({getTableProps:n,getTableBodyProps:e,prepareRow:t,headerGroups:a,columns:o,rows:i,loading:s,highlightRowId:g,columnsForWrapText:u})=>(0,c.tZ)(p,l()({},n(),{className:"table table-hover","data-test":"listview-table"}),(0,c.tZ)("thead",null,a.map((n=>(0,c.tZ)("tr",n.getHeaderGroupProps(),n.headers.map((n=>{let e=(0,c.tZ)(d.Z.Sort,null);return n.isSorted&&n.isSortedDesc?e=(0,c.tZ)(d.Z.SortDesc,null):n.isSorted&&!n.isSortedDesc&&(e=(0,c.tZ)(d.Z.SortAsc,null)),n.hidden?null:(0,c.tZ)("th",l()({},n.getHeaderProps(n.canSort?n.getSortByToggleProps():{}),{"data-test":"sort-header",className:r()({[n.size||""]:n.size})}),(0,c.tZ)("span",null,n.render("Header"),n.canSort&&e))})))))),(0,c.tZ)("tbody",e(),s&&0===i.length&&[...new Array(12)].map(((n,e)=>(0,c.tZ)("tr",{key:e},o.map(((n,e)=>n.hidden?null:(0,c.tZ)("td",{key:e,className:r()("table-cell",{"table-cell-loader":s})},(0,c.tZ)("span",{className:"loading-bar empty-loading-bar",role:"progressbar","aria-label":"loading"}))))))),i.length>0&&i.map((n=>{t(n);const e=n.original.id;return(0,c.tZ)("tr",l()({"data-test":"table-row"},n.getRowProps(),{className:r()("table-row",{"table-row-selected":n.isSelected||"undefined"!==typeof e&&e===g})}),n.cells.map((n=>{if(n.column.hidden)return null;const e=n.column.cellProps||{},t=null==u?void 0:u.includes(n.column.Header);return(0,c.tZ)("td",l()({"data-test":"table-row-cell",className:r()("table-cell table-cell__"+(t?"wrap":"nowrap"),{"table-cell-loader":s,[n.column.size||""]:n.column.size})},n.getCellProps(),e),(0,c.tZ)("span",{className:r()({"loading-bar":s}),role:s?"progressbar":void 0},(0,c.tZ)("span",{"data-test":"cell-text"},n.render("Cell"))))})))}))))))},946977:(n,e,t)=>{t.d(e,{Z:()=>f,u:()=>h});var a=t(205872),l=t.n(a),o=t(667294),i=t(618446),r=t.n(i),s=t(751995),d=t(455867),c=t(379521),p=t(49937),g=t(64158),u=t(397754),m=t(211965);var h;!function(n){n.Default="Default",n.Small="Small"}(h||(h={}));const b=s.iK.div`
  margin: ${({theme:n})=>40*n.gridUnit}px 0;
`,x=s.iK.div`
  ${({scrollTable:n,theme:e})=>n&&`\n    flex: 1 1 auto;\n    margin-bottom: ${4*e.gridUnit}px;\n    overflow: auto;\n  `}

  .table-row {
    ${({theme:n,small:e})=>!e&&`height: ${11*n.gridUnit-1}px;`}

    .table-cell {
      ${({theme:n,small:e})=>e&&`\n        padding-top: ${n.gridUnit+1}px;\n        padding-bottom: ${n.gridUnit+1}px;\n        line-height: 1.45;\n      `}
    }
  }

  th[role='columnheader'] {
    z-index: 1;
    border-bottom: ${({theme:n})=>`${n.gridUnit-2}px solid ${n.colors.grayscale.light2}`};
    ${({small:n})=>n&&"padding-bottom: 0;"}
  }
`,y=s.iK.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: ${({theme:n})=>n.colors.grayscale.light5};

  ${({isPaginationSticky:n})=>n&&"\n        position: sticky;\n        bottom: 0;\n        left: 0;\n    "};

  .row-count-container {
    margin-top: ${({theme:n})=>2*n.gridUnit}px;
    color: ${({theme:n})=>n.colors.grayscale.base};
  }
`,w=({columns:n,data:e,pageSize:t,totalCount:a=e.length,initialPageIndex:i,initialSortBy:s=[],loading:w=!1,withPagination:f=!0,emptyWrapperType:Z=h.Default,noDataText:k,showRowCount:v=!0,serverPagination:P=!1,columnsForWrapText:S,onServerPagination:$=(()=>{}),scrollTopOnPagination:C=!1,...I})=>{const T={pageSize:null!=t?t:10,pageIndex:null!=i?i:0,sortBy:s},{getTableProps:N,getTableBodyProps:E,headerGroups:_,page:B,rows:A,prepareRow:D,pageCount:z,gotoPage:R,state:{pageIndex:G,pageSize:L,sortBy:U}}=(0,c.useTable)({columns:n,data:e,initialState:T,manualPagination:P,manualSortBy:P,pageCount:Math.ceil(a/T.pageSize)},c.useFilters,c.useSortBy,c.usePagination),K=f?B:A;let F;switch(Z){case h.Small:F=({children:n})=>(0,m.tZ)(o.Fragment,null,n);break;case h.Default:default:F=({children:n})=>(0,m.tZ)(b,null,n)}const H=!w&&0===K.length,M=z>1&&f,W=(0,o.useRef)(null);return(0,o.useEffect)((()=>{P&&G!==T.pageIndex&&$({pageIndex:G})}),[G]),(0,o.useEffect)((()=>{P&&!r()(U,T.sortBy)&&$({pageIndex:0,sortBy:U})}),[U]),(0,m.tZ)(o.Fragment,null,(0,m.tZ)(x,l()({},I,{ref:W}),(0,m.tZ)(u.Z,{getTableProps:N,getTableBodyProps:E,prepareRow:D,headerGroups:_,rows:K,columns:n,loading:w,columnsForWrapText:S}),H&&(0,m.tZ)(F,null,k?(0,m.tZ)(p.HY,{image:p.HY.PRESENTED_IMAGE_SIMPLE,description:k}):(0,m.tZ)(p.HY,{image:p.HY.PRESENTED_IMAGE_SIMPLE}))),M&&(0,m.tZ)(y,{className:"pagination-container",isPaginationSticky:I.isPaginationSticky},(0,m.tZ)(g.Z,{totalPages:z||0,currentPage:z?G+1:0,onChange:n=>(n=>{var e;C&&(null==W||null==(e=W.current)||e.scroll(0,0)),R(n)})(n-1),hideFirstAndLastPageLinks:!0}),v&&(0,m.tZ)("div",{className:"row-count-container"},!w&&(0,d.t)("%s-%s of %s",L*G+(B.length&&1),L*G+B.length,a))))},f=o.memo(w)},676962:(n,e,t)=>{t.d(e,{Z:()=>a.Z,u:()=>a.u});var a=t(946977)}}]);