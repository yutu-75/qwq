"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[89483],{89483:(e,t,a)=>{a.r(t),a.d(t,{default:()=>m});var r=a(751995),i=a(5364),o=a(667294),l=a(101090),n=a(174448),s=a(828216),u=a(52004),d=a(454076),v=a(211965);const h=(0,r.iK)(n.un)`
  display: flex;
  align-items: center;
  overflow-x: auto;

  & .ant-tag {
    margin-right: 0;
  }
`,c=r.iK.div`
  display: flex;
  height: 100%;
  max-width: 100%;
  width: 100%;
  & > div,
  & > div:hover {
    ${({validateStatus:e,theme:t})=>{var a;return e&&`border-color: ${null==(a=t.colors[e])?void 0:a.base}`}}
  }
`;function m(e){var t;const{setDataMask:a,setHoveredFilter:r,unsetHoveredFilter:n,setFocusedFilter:m,unsetFocusedFilter:f,setFilterActive:g,width:p,height:w,filterState:F,inputRef:b,isOverflowingFilterBar:k=!1,formData:x}=e,C=(0,o.useCallback)((e=>{const t=e&&e!==i.vM;a({extraFormData:t?{time_range:e}:{},filterState:{value:t?e:void 0}})}),[a]);(0,o.useEffect)((()=>{C(F.value)}),[F.value]);const y=(0,s.v9)((({dashboardInfo:e})=>{var t;return(null==e||null==(t=e.metadata)?void 0:t.layout_type)||"rowAndColumn"})),M=(0,s.v9)((e=>e.dashboardState.layoutMode||u.kB.PC)),S=(0,d.Od)(M);return null!=(t=e.formData)&&t.inView?(0,v.tZ)(h,{width:p,height:w,style:!p&&S&&"grid"!==y?{width:"auto"}:{}},(0,v.tZ)(c,{ref:b,validateStatus:F.validateStatus,onFocus:m,onBlur:f,onMouseEnter:r,onMouseLeave:n},(0,v.tZ)(l.ZP,{formData:x,value:F.value||i.vM,name:"time_range",onChange:C,onOpenPopover:()=>g(!0),onClosePopover:()=>{g(!1),n(),f()},isOverflowingFilterBar:k}))):null}},174448:(e,t,a)=>{a.d(t,{Am:()=>n,jp:()=>l,un:()=>o});var r=a(751995),i=a(804591);const o=r.iK.div`
  min-height: ${({height:e})=>e}px;
  width: ${({width:e})=>e}px;
`,l=(0,r.iK)(i.Z)`
  &.ant-row.ant-form-item {
    margin: 0;
  }
`,n=r.iK.div`
  color: ${({theme:e,status:t="error"})=>{var a;return null==(a=e.colors[t])?void 0:a.base}};
`}}]);