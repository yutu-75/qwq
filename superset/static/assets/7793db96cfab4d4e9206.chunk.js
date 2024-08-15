"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[16968],{616968:(t,e,n)=>{n.r(e),n.d(e,{default:()=>O});n(667294);var r=n(943323),a=n(751995),i=n(644059);var o=n(694017);function u(t){t.x0=Math.round(t.x0),t.y0=Math.round(t.y0),t.x1=Math.round(t.x1),t.y1=Math.round(t.y1)}function s(t,e,n,r,a){for(var i,o=t.children,u=-1,s=o.length,c=t.value&&(r-e)/t.value;++u<s;)(i=o[u]).y0=n,i.y1=a,i.x0=e,i.x1=e+=i.value*c}function c(t,e,n,r,a){for(var i,o=t.children,u=-1,s=o.length,c=t.value&&(a-n)/t.value;++u<s;)(i=o[u]).x0=e,i.x1=r,i.y0=n,i.y1=n+=i.value*c}const p=function t(e){function n(t,n,r,a,i){!function(t,e,n,r,a,i){for(var o,u,p,h,l,d,f,g,m,v,y,x=[],b=e.children,w=0,T=0,A=b.length,$=e.value;w<A;){p=a-n,h=i-r;do{l=b[T++].value}while(!l&&T<A);for(d=f=l,y=l*l*(v=Math.max(h/p,p/h)/($*t)),m=Math.max(f/y,y/d);T<A;++T){if(l+=u=b[T].value,u<d&&(d=u),u>f&&(f=u),y=l*l*v,(g=Math.max(f/y,y/d))>m){l-=u;break}m=g}x.push(o={value:l,dice:p<h,children:b.slice(w,T)}),o.dice?s(o,n,r,a,$?r+=h*l/$:i):c(o,n,r,$?n+=p*l/$:a,i),$-=l,w=T}}(e,t,n,r,a,i)}return n.ratio=function(e){return t((e=+e)>1?e:1)},n}((1+Math.sqrt(5))/2);function h(t){if("function"!==typeof t)throw new Error;return t}function l(){return 0}function d(t){return function(){return t}}var f=n(671939),g=n(45697),m=n.n(g),v=n(767190),y=n(328062);const x=m().shape({name:m().string,value:m().number.isRequired}),b={name:m().string,children:m().arrayOf(m().oneOfType([m().shape((w=()=>b,()=>w().apply(void 0,arguments))),x]))};var w;const T=m().oneOfType([m().shape(b),x]),A={data:m().arrayOf(T),width:m().number,height:m().number,colorScheme:m().string,margin:m().shape({top:m().number,right:m().number,bottom:m().number,left:m().number}),numberFormat:m().string,treemapRatio:m().number};function $(t){return function(e){var n;(n=e.ancestors().map((t=>t.node)),"string"===typeof n?new i.Y1([document.querySelectorAll(n)],[document.documentElement]):new i.Y1([null==n?[]:n],i.Jz)).classed("node--hover",t).select("rect").attr("width",(e=>e.x1-e.x0-t)).attr("height",(e=>e.y1-e.y0-t))}}function Z(t,e){const{data:n,width:r,height:a,numberFormat:i,colorScheme:s,treemapRatio:c,sliceId:g}=e,m=(0,o.Z)(t);m.classed("superset-legacy-chart-treemap",!0);const x=(0,v.JB)(i),b=y.getScale(s),w=n;if(m.selectAll("*").remove(),w.length>0){const[t]=w,e=function(){var t=p,e=!1,n=1,r=1,a=[0],i=l,o=l,s=l,c=l,f=l;function g(t){return t.x0=t.y0=0,t.x1=n,t.y1=r,t.eachBefore(m),a=[0],e&&t.eachBefore(u),t}function m(e){var n=a[e.depth],r=e.x0+n,u=e.y0+n,p=e.x1-n,h=e.y1-n;p<r&&(r=p=(r+p)/2),h<u&&(u=h=(u+h)/2),e.x0=r,e.y0=u,e.x1=p,e.y1=h,e.children&&(n=a[e.depth+1]=i(e)/2,r+=f(e)-n,u+=o(e)-n,(p-=s(e)-n)<r&&(r=p=(r+p)/2),(h-=c(e)-n)<u&&(u=h=(u+h)/2),t(e,r,u,p,h))}return g.round=function(t){return arguments.length?(e=!!t,g):e},g.size=function(t){return arguments.length?(n=+t[0],r=+t[1],g):[n,r]},g.tile=function(e){return arguments.length?(t=h(e),g):t},g.padding=function(t){return arguments.length?g.paddingInner(t).paddingOuter(t):g.paddingInner()},g.paddingInner=function(t){return arguments.length?(i="function"===typeof t?t:d(+t),g):i},g.paddingOuter=function(t){return arguments.length?g.paddingTop(t).paddingRight(t).paddingBottom(t).paddingLeft(t):g.paddingTop()},g.paddingTop=function(t){return arguments.length?(o="function"===typeof t?t:d(+t),g):o},g.paddingRight=function(t){return arguments.length?(s="function"===typeof t?t:d(+t),g):s},g.paddingBottom=function(t){return arguments.length?(c="function"===typeof t?t:d(+t),g):c},g.paddingLeft=function(t){return arguments.length?(f="function"===typeof t?t:d(+t),g):f},g}().size([r,a]).paddingOuter(3).paddingTop(19).paddingInner(1).tile(p.ratio(c)).round(!0),n=e((0,f.ZP)(t).sum((t=>t.value)).sort(((t,e)=>e.height-t.height||e.value-t.value))),i=m.append("svg").attr("class","treemap").attr("width",r).attr("height",a).selectAll(".node").data(n.descendants()).enter().append("g").attr("transform",(t=>`translate(${t.x0},${t.y0})`)).attr("class","node").each((function(t){t.node=this})).on("mouseover",$(!0)).on("mouseout",$(!1));i.append("rect").attr("id",(t=>`rect-${t.data.name}`)).attr("width",(t=>t.x1-t.x0)).attr("height",(t=>t.y1-t.y0)).style("fill",(t=>b(t.depth,g))),i.append("clipPath").attr("id",(t=>`clip-${t.data.name}`)).append("use").attr("xlink:href",(t=>`#rect-${t.data.name}`));const o=i.append("text").attr("clip-path",(t=>`url(#clip-${t.data.name})`));o.filter((t=>t.children)).selectAll("tspan").data((t=>t.data.name.slice(Math.max(0,t.data.name.lastIndexOf(".")+1)).split(/(?=[A-Z][^A-Z])/g).concat(`\xa0${x(t.value)}`))).enter().append("tspan").attr("x",((t,e)=>e?null:4)).attr("y",13).text((t=>t)),o.filter((t=>!t.children)).selectAll("tspan").data((t=>t.data.name.slice(Math.max(0,t.data.name.lastIndexOf(".")+1)).split(/(?=[A-Z][^A-Z])/g).concat(x(t.value)))).enter().append("tspan").attr("x",4).attr("y",((t,e)=>13+10*e)).text((t=>t)),i.append("title").text((t=>`${t.data.name}\n${x(t.value)}`))}}Z.displayName="Treemap",Z.propTypes=A;const M=Z;var B=n(211965);const k=(0,r.Z)(M),O=(0,a.iK)((({className:t,...e})=>(0,B.tZ)("div",{className:t},(0,B.tZ)(k,e))))`
  ${({theme:t})=>`\n    .superset-legacy-chart-treemap text {\n      font-size: ${t.typography.sizes.s}px;\n      pointer-events: none;\n    }\n\n    .superset-legacy-chart-treemap tspan:last-child {\n      font-size: ${t.typography.sizes.xs}px;\n      fill-opacity: 0.8;\n    }\n\n    .superset-legacy-chart-treemap .node rect {\n      shape-rendering: crispEdges;\n    }\n\n    .superset-legacy-chart-treemap .node--hover rect {\n      stroke: ${t.colors.grayscale.dark2};\n    }\n  `}
`},671939:(t,e,n)=>{function r(t){var e=0,n=t.children,r=n&&n.length;if(r)for(;--r>=0;)e+=n[r].value;else e=1;t.value=e}function a(t,e){var n,r,a,o,c,p=new s(t),h=+t.value&&(p.value=t.value),l=[p];for(null==e&&(e=i);n=l.pop();)if(h&&(n.value=+n.data.value),(a=e(n.data))&&(c=a.length))for(n.children=new Array(c),o=c-1;o>=0;--o)l.push(r=n.children[o]=new s(a[o])),r.parent=n,r.depth=n.depth+1;return p.eachBefore(u)}function i(t){return t.children}function o(t){t.data=t.data.data}function u(t){var e=0;do{t.height=e}while((t=t.parent)&&t.height<++e)}function s(t){this.data=t,this.depth=this.height=0,this.parent=null}n.d(e,{ZP:()=>a}),s.prototype=a.prototype={constructor:s,count:function(){return this.eachAfter(r)},each:function(t){var e,n,r,a,i=this,o=[i];do{for(e=o.reverse(),o=[];i=e.pop();)if(t(i),n=i.children)for(r=0,a=n.length;r<a;++r)o.push(n[r])}while(o.length);return this},eachAfter:function(t){for(var e,n,r,a=this,i=[a],o=[];a=i.pop();)if(o.push(a),e=a.children)for(n=0,r=e.length;n<r;++n)i.push(e[n]);for(;a=o.pop();)t(a);return this},eachBefore:function(t){for(var e,n,r=this,a=[r];r=a.pop();)if(t(r),e=r.children)for(n=e.length-1;n>=0;--n)a.push(e[n]);return this},sum:function(t){return this.eachAfter((function(e){for(var n=+t(e.data)||0,r=e.children,a=r&&r.length;--a>=0;)n+=r[a].value;e.value=n}))},sort:function(t){return this.eachBefore((function(e){e.children&&e.children.sort(t)}))},path:function(t){for(var e=this,n=function(t,e){if(t===e)return t;var n=t.ancestors(),r=e.ancestors(),a=null;t=n.pop(),e=r.pop();for(;t===e;)a=t,t=n.pop(),e=r.pop();return a}(e,t),r=[e];e!==n;)e=e.parent,r.push(e);for(var a=r.length;t!==n;)r.splice(a,0,t),t=t.parent;return r},ancestors:function(){for(var t=this,e=[t];t=t.parent;)e.push(t);return e},descendants:function(){var t=[];return this.each((function(e){t.push(e)})),t},leaves:function(){var t=[];return this.eachBefore((function(e){e.children||t.push(e)})),t},links:function(){var t=this,e=[];return t.each((function(n){n!==t&&e.push({source:n.parent,target:n})})),e},copy:function(){return a(this).eachBefore(o)}}},943323:(t,e,n)=>{n.d(e,{Z:()=>i});var r=n(667294),a=n(211965);function i(t,e){class n extends r.Component{constructor(t){super(t),this.container=void 0,this.setContainerRef=this.setContainerRef.bind(this)}componentDidMount(){this.execute()}componentDidUpdate(){this.execute()}componentWillUnmount(){this.container=void 0,null!=e&&e.componentWillUnmount&&e.componentWillUnmount.bind(this)()}setContainerRef(t){this.container=t}execute(){this.container&&t(this.container,this.props)}render(){const{id:t,className:e}=this.props;return(0,a.tZ)("div",{ref:this.setContainerRef,id:t,className:e})}}const i=n;return t.displayName&&(i.displayName=t.displayName),t.propTypes&&(i.propTypes={...i.propTypes,...t.propTypes}),t.defaultProps&&(i.defaultProps=t.defaultProps),n}}}]);