"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[40127],{596638:(t,e,i)=>{i.d(e,{Z:()=>d});var n=i(260229),a=i(667294),l=i(592770);const d=function(t){var e=(0,n.CR)((0,a.useState)(t),2),i=e[0],d=e[1];return[i,(0,a.useCallback)((function(t){d((function(e){var i=(0,l.mf)(t)?t(e):t;return i?(0,n.pi)((0,n.pi)({},e),i):e}))}),[])]}},340127:(t,e,i)=>{i.r(e),i.d(e,{default:()=>y});var n=i(667294),a=i(596638),l=i(294184),d=i.n(l),o=i(71577),s=i(519650),c=i(3006),r=i(751995),u=i(619702),p=i(958452),Z=i(807500),k=i(432615),h=i(211965);const m=({onClick:t,title:e})=>(0,h.tZ)(o.Z,{icon:(0,h.tZ)(k.default,null),onClick:t,type:"primary"},e),C=r.iK.div`
  display: ${({hide:t})=>t?"none":"block"};
`,g=(0,r.iK)((({className:t,text:e,onClick:i})=>(0,h.tZ)(o.Z,{type:"default",className:t,onClick:i},e)))`
  margin-right: 20px;
`,f=t=>{const{onIncrease:e,title:i,isCustom:a,children:l}=t;return(0,h.tZ)(s.Z,{align:"center"},(0,h.tZ)("span",{className:d()("api-link-title")},i),a?n.Children.only(l):(0,h.tZ)(m,{onClick:e,title:i}))},y=()=>{const[t,e]=(0,a.Z)({data:[],loading:!1,modalOpen:!1,pagination:{current:1,pageSize:20}});(0,n.useEffect)((()=>{}),[]);const i={rowKey:"id",bordered:!1,size:"middle",columns:[{title:"\u540d\u79f0",dataIndex:"name",width:150,ellipsis:!0},{title:"\u7c7b\u578b",dataIndex:"type",width:80},{title:"\u63cf\u8ff0",dataIndex:"description",width:250,ellipsis:!0},{title:"\u521b\u5efa\u4eba",dataIndex:"personal",width:100},{title:"\u6700\u540e\u4fee\u6539",dataIndex:"modify last",width:150},{title:"\u64cd\u4f5c",key:"operation",width:100,render:(t,e)=>[(0,h.tZ)("a",{onClick:()=>{},key:"button-delete"},(0,h.tZ)(u.default,null)),(0,h.tZ)("a",{onClick:()=>{},key:"button-edit"},(0,h.tZ)(p.default,null))]}],dataSource:t.data,loading:t.loading,pagination:t.pagination,onChange:(t,e,i)=>{}},l=()=>{};return(0,h.tZ)("div",{className:d()("api-link-content","api-link-bg")},(0,h.tZ)(C,{hide:!1},(0,h.tZ)(f,{title:"API",onIncrease:()=>e({modalOpen:!0})}),(0,h.tZ)(c.Z,i)),(0,h.tZ)(C,{hide:!0},(0,h.tZ)(f,{isCustom:!0,title:(0,h.tZ)("a",{onClick:()=>null},(0,h.tZ)(Z.default,null),"\u65b0\u5efaAPI\u6570\u636e\u6e90")},(0,h.tZ)("div",null,(0,h.tZ)(g,{text:"\u53d6\u6d88",onClick:l}),(0,h.tZ)(g,{text:"\u6821\u9a8c",onClick:l}),(0,h.tZ)(o.Z,{type:"primary"},"\u4e0b\u4e00\u6b65"))),(0,h.tZ)("div",{className:"api-link-block"},(0,h.tZ)("div",{className:"api-link-center"}))))}}}]);